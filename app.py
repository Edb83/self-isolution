import os
import boto3
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from datetime import date
from io import BytesIO
from PIL import Image, ImageOps

if os.path.exists("env.py"):
    import env

# Amazon S3 Bucket
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}

S3_BUCKET = os.environ.get("S3_BUCKET")
S3_KEY = os.environ.get("S3_KEY")
S3_SECRET = os.environ.get("S3_SECRET_ACCESS_KEY")
S3_LOCATION = os.environ.get("S3_LOCATION")

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")
app.config['MAX_CONTENT_LENGTH'] = 8 * 1024 * 1024

mongo = PyMongo(app)

s3 = boto3.client(
    "s3",
    aws_access_key_id=S3_KEY,
    aws_secret_access_key=S3_SECRET
)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def upload_file():
    output = ""

    """
    Check the request.files object for an image_file key.
    (image_file is the name of the file input in add_activity, edit_activity, add_category and edit_category)
    If it's not there, return blank output (for handling default images where necessary)
    """
    if "image_file" not in request.files:
        return output

    # If the key is in the object, save it in file variable
    file = request.files["image_file"]

    """
    Check the filename attribute on the object
    If empty, it means the user sumbmitted an empty form, so return a blank output
    """
    if file.filename == "":
        return output

    # Check that there is a file and that it has an allowed filetype
    if file and allowed_file(file.filename):
        file.filename = secure_filename(file.filename)
        output = upload_file_to_s3(file)

    return output


def resize_image(file):
    # Load image
    raw_image = Image.open(file)

    # Save format (as not copied on creation of new image)
    saved_format = raw_image.format

    # Read EXIF data to handle portrait images being rotated
    new_image = ImageOps.exif_transpose(raw_image)

    # Reapply raw_image format
    new_image.format = saved_format

    # Resize image and set max-length in either axis
    new_image.thumbnail((500, 500))

    # Save the image to an in-memory file
    in_mem_file = BytesIO()
    new_image.save(in_mem_file, format=new_image.format)

    # 'Rewind' the file-like object to prevent 0kb-sized files
    in_mem_file.seek(0)

    return in_mem_file


def upload_file_to_s3(file):
    try:
        image_for_upload = resize_image(file)

        # Upload image to s3
        s3.upload_fileobj(
            image_for_upload,
            S3_BUCKET,
            file.filename,
            ExtraArgs={
                'ACL': 'public-read'
            }
        )

    except Exception as e:
        print("Something Happened: ", e)
        return e

    return "{}{}".format(S3_LOCATION, file.filename)


@app.route("/")
@app.route("/home")
def home():
    activities = list(mongo.db.activities.find().sort("_id", -1))
    categories = list(mongo.db.categories.find())

    return render_template("home.html", activities=activities, categories=categories)


@app.route("/activities")
def get_activities():
    activities = list(mongo.db.activities.find().sort("_id", -1))
    categories = list(mongo.db.categories.find())

    return render_template(
        "activities.html", activities=activities, categories=categories, page_heading="All Activities")


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    activities = list(mongo.db.activities.find({"$text": {"$search": query}}).sort("_id", -1))
    return render_template("activities.html", activities=activities,
                           page_heading=f"Results for '{query}'")


@app.route("/filter/category/<category_id>")
def filter_category(category_id):
    categories = list(mongo.db.categories.find())
    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    activities = list(mongo.db.activities.find(
        {"category_name": category["category_name"]}).sort("_id", -1))

    return render_template("activities.html", category=category,
                           activities=activities, categories=categories,
                           page_heading=f"Activities for {category['category_name']}")


@app.route("/filter/age/<target_age>")
def filter_age(target_age):
    categories = list(mongo.db.categories.find())
    activities = list(mongo.db.activities.find(
        {"target_age": target_age}).sort("_id", -1))

    return render_template("activities.html",
                           activities=activities, categories=categories,
                           page_heading=f"Activities for {target_age.lower()} years old")


@app.route("/filter/user/<username>")
def filter_user(username):
    categories = list(mongo.db.categories.find())
    activities = list(mongo.db.activities.find(
        {"created_by": username}).sort("_id", -1))

    return render_template("activities.html",
                           activities=activities, categories=categories,
                           page_heading=f"Activities from {username}")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username '{}' aleady exists".format(request.form.get("username")))
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Logged in as {}".format(request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))

            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
            # username does not exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # get session user's username from database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    activities = list(mongo.db.activities.find(
        {"created_by": session["user"]}).sort("_id", -1))
    categories = list(mongo.db.categories.find())

    if session["user"]:
        return render_template(
            "profile.html", username=username,
            activities=activities, categories=categories)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_activity", methods=["GET", "POST"])
def add_activity():
    ages = ["Under 2", "2-4", "4-6", "6+"]
    categories = list(mongo.db.categories.find().sort("category_name", 1))

    if request.method == "POST":
        activity = {
            "activity_name": request.form.get("activity_name"),
            "category_name": request.form.get("category_name"),
            "target_age": request.form.get("target_age"),
            "activity_summary": request.form.get("activity_summary"),
            "activity_details": request.form.get("activity_details"),
            "activity_equipment": request.form.get("activity_equipment"),
            "image_file": upload_file(),
            "created_by": session["user"],
            "date_added": date.today().strftime("%d %b %Y")
        }

        existing_activities = mongo.db.activities.find({"activity_name": activity["activity_name"]})

        if any(d["activity_name"] == activity["activity_name"] for d in existing_activities):
            flash("'{}' already exists, please choose another name".format(activity["activity_name"]))
            return redirect(url_for("add_activity"))

        else:
            new_activity = mongo.db.activities.insert_one(activity).inserted_id
            mongo.db.categories.update_one(
                {"category_name": activity["category_name"]}, {"$push": {"activity_list": ObjectId(new_activity)}})
            flash("Activity added: {}".format(activity["activity_name"]))
            return redirect(url_for("get_activities"))

    return render_template(
        "add_activity.html", categories=categories, ages=ages)


@app.route("/edit_activity/<activity_id>", methods=["GET", "POST"])
def edit_activity(activity_id):
    activity = mongo.db.activities.find_one({"_id": ObjectId(activity_id)})
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    ages = ["Under 2", "2-4", "4-6", "6+"]

    current_category = mongo.db.categories.find_one({"category_name": activity["category_name"]})

    if request.method == "POST":
        if request.files["image_file"].filename == "":
            edit_image_path = activity["image_file"]
        else:
            edit_image_path = upload_file()

        edit = {"$set": {
            "activity_name": request.form.get("activity_name"),
            "category_name": request.form.get("category_name"),
            "target_age": request.form.get("target_age"),
            "activity_summary": request.form.get("activity_summary"),
            "activity_details": request.form.get("activity_details"),
            "activity_equipment": request.form.get("activity_equipment"),
            "image_file": edit_image_path,
        }}
        existing_activities = mongo.db.activities.find({"activity_name": request.form.get("activity_name")})
        if request.form.get("activity_name") != activity["activity_name"] and any(
            d["activity_name"] == request.form.get(
                "activity_name") for d in existing_activities):
            flash("'{}' already exists, please choose another name".format(request.form.get("activity_name")))
            return render_template(
                "edit_activity.html",
                activity=activity,
                categories=categories,
                ages=ages)
        else:
            mongo.db.activities.update_many(activity, edit)
            new_category = mongo.db.categories.find_one(
                {"category_name": request.form.get("category_name")})

            if request.form.get("category_name") != current_category["category_name"]:
                mongo.db.categories.update_one(
                    new_category,
                    {"$push": {"activity_list": activity["_id"]}})
                mongo.db.categories.update_one(
                    current_category,
                    {"$pull": {"activity_list": activity["_id"]}})

            flash("Activity updated ({})".format(activity["activity_name"]))
            return redirect(url_for('view_activity', activity_id=ObjectId(activity_id)))

    return render_template(
        "edit_activity.html",
        activity=activity,
        categories=categories,
        ages=ages)


@app.route("/delete_activity/<activity_id>")
def delete_activity(activity_id):
    activity = mongo.db.activities.find_one({"_id": ObjectId(activity_id)})
    current_category = mongo.db.categories.find_one({"category_name": activity["category_name"]})
    mongo.db.categories.update_one(
        current_category,
        {"$pull": {"activity_list": activity["_id"]}})

    mongo.db.activities.remove({"_id": ObjectId(activity_id)})

    flash("Activity deleted ({})".format(activity["activity_name"]))
    return redirect(url_for('profile', username=session['user']))


@app.route("/view_activity/<activity_id>")
def view_activity(activity_id):
    activity = mongo.db.activities.find_one({"_id": ObjectId(activity_id)})
    user = mongo.db.users.find_one({"username": activity["created_by"]})
    categories = list(mongo.db.categories.find())
    return render_template("view_activity.html", activity=activity,
                           categories=categories, user=user)


@app.route("/categories")
def get_categories():
    activities = list(mongo.db.activities.find())
    categories = list(mongo.db.categories.find().sort("category_name", 1))

    return render_template("categories.html", categories=categories, activities=activities)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name"),
            "category_summary": request.form.get("category_summary"),
            "image_file": upload_file(),
            "activity_list": []
        }

        mongo.db.categories.insert_one(category)
        flash("Category added ({})".format(category["category_name"]))
        return redirect(url_for("get_categories"))

    return render_template(
        "add_category.html")


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})

    if request.method == "POST":
        if request.files["image_file"].filename == "":
            edit_image_path = category["image_file"]
        else:
            edit_image_path = upload_file()
        submit = {"$set": {
            "category_summary": request.form.get("category_summary"),
            "image_file": edit_image_path,
        }}
        mongo.db.categories.update_many(category, submit)
        flash("Category updated ({})".format(category["category_name"]))
        return redirect(url_for("get_categories"))

    return render_template(
        "edit_category.html", category=category)


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    # find the category
    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    # get all activities with that category name
    dependent_activities = list(mongo.db.activities.find(
        {"category_name": category["category_name"]}))
    # find the category of "Unassigned"
    unassigned_category = mongo.db.categories.find_one(
        {"category_name": "Unassigned"})
    # prepare an empty list
    activities = []
    for activity in dependent_activities:
        # update the "category_name" to "Unassigned"
        mongo.db.activities.find_one_and_update(
            activity, {"$set": {"category_name": "Unassigned"}})
        # append this ObjectID to the activities list
        activities.append(activity["_id"])
    # push each activity into the "Unassigned" category's activity_list key
    mongo.db.categories.find_one_and_update(
        unassigned_category, {"$addToSet": {"activity_list": {"$each": activities}}})

    # remove the category from MongoDB
    mongo.db.categories.remove(category)

    flash("Category deleted ({})".format(category["category_name"]))
    return redirect(url_for('get_categories'))


@app.errorhandler(404)
def not_found(error):
    '''
    Handles any 404 error
    '''
    return render_template('404.html', error=error), 404


@app.errorhandler(500)
def internal_error(error):
    '''
    Handles any 500 error
    '''
    return render_template('500.html', error=error), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
