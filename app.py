import os
import boto3
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from flask_paginate import Pagination, get_page_args
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from datetime import date
from io import BytesIO
from PIL import Image, ImageOps

if os.path.exists("env.py"):
    import env  # noqa: F401

# Amazon S3 Bucket
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}

S3_BUCKET = os.environ.get("S3_BUCKET")
S3_KEY = os.environ.get("S3_KEY")
S3_SECRET = os.environ.get("S3_SECRET_ACCESS_KEY")
S3_LOCATION = os.environ.get("S3_LOCATION")

AGES = ["Under 2", "2-4", "4-6", "6+"]

PER_PAGE = 9

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

# FUNCTIONS


# Pagination
def paginated(activities):
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
    offset = page * PER_PAGE - PER_PAGE

    return activities[offset: offset + PER_PAGE]


def pagination_args(activities):
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
    total = len(activities)

    return Pagination(page=page, per_page=PER_PAGE, total=total)


# Image upload
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


# ROUTING

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
    activities_paginated = paginated(activities)
    pagination = pagination_args(activities)

    return render_template('activities.html',
                           activities=activities_paginated,
                           categories=categories,
                           page_heading="All Activities",
                           pagination=pagination,
                           )


@app.route("/search")
def search():

    query = request.args.get("query")
    categories = list(mongo.db.categories.find())
    activities = list(mongo.db.activities.find({"$text": {"$search": query}}).sort("_id", -1))
    activities_paginated = paginated(activities)
    pagination = pagination_args(activities)

    return render_template("activities.html", categories=categories,
                           activities=activities_paginated, pagination=pagination,
                           page_heading="Results for '{}'".format(query))


@app.route("/filter/category/<category_id>")
def filter_category(category_id):

    categories = list(mongo.db.categories.find())
    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    activities = list(mongo.db.activities.find(
        {"category_name": category["category_name"]}).sort("_id", -1))
    activities_paginated = paginated(activities)
    pagination = pagination_args(activities)

    return render_template("activities.html", category=category,
                           activities=activities_paginated, categories=categories, pagination=pagination,
                           page_heading=category['category_name'])


@app.route("/filter/age/<target_age>")
def filter_age(target_age):

    categories = list(mongo.db.categories.find())
    activities = list(mongo.db.activities.find(
        {"target_age": target_age}).sort("_id", -1))
    activities_paginated = paginated(activities)
    pagination = pagination_args(activities)

    return render_template("activities.html",
                           activities=activities_paginated, categories=categories, pagination=pagination,
                           page_heading=target_age)


@app.route("/filter/user/<username>")
def filter_user(username):

    categories = list(mongo.db.categories.find())
    activities = list(mongo.db.activities.find(
        {"created_by": username}).sort("_id", -1))
    activities_paginated = paginated(activities)
    pagination = pagination_args(activities)

    return render_template("activities.html",
                           activities=activities_paginated, categories=categories, pagination=pagination,
                           page_heading="Activities from {}".format(username))


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method != "POST":
        return render_template("register.html")

    else:
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


@app.route("/login", methods=["GET", "POST"])
def login():

    if "user" in session:
        return redirect(url_for(
                "profile", username=session["user"]))

    elif request.method != "POST":
        return render_template("login.html")

    else:
        # check if username exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if not existing_user:
            flash("Incorrect Username and/or Password")

            return redirect(url_for("login"))

        # ensure hashed password matches user input
        elif check_password_hash(
                existing_user["password"], request.form.get("password")):
            session["user"] = request.form.get("username").lower()
            flash("Logged in as {}".format(request.form.get("username")))

            return redirect(url_for(
                "profile", username=session["user"]))

        else:
            flash("Incorrect Username and/or Password")

            return redirect(url_for("login"))


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):

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

    if "user" not in session:
        flash("You are already logged out!")

        return redirect(url_for("home"))
    else:
        # remove user from session cookies
        flash("You have been logged out")
        session.pop("user")

        return redirect(url_for("login"))


@app.route("/add_activity", methods=["GET", "POST"])
def add_activity():

    categories = list(mongo.db.categories.find().sort("category_name", 1))

    if "user" not in session:
        flash("You need to Log In to do that!")

        return redirect(url_for("login"))

    elif request.method != "POST":
        return render_template(
            "add_activity.html", categories=categories, ages=AGES)

    else:
        # get new activity details
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

        # create a list of activity names
        activities = list(mongo.db.activities.find())
        lowercase_name = activity["activity_name"].lower()
        lowercase_list = []
        for x in activities:
            lowercase_list.append(x["activity_name"].lower())

        # check whether name already taken
        if lowercase_name in lowercase_list:
            flash("'{}' already exists, please choose another name".format(activity["activity_name"]))

            return redirect(url_for("add_activity"))

        # otherwise add activity to the database and store activity id in category's activity_list
        else:
            new_activity = mongo.db.activities.insert_one(activity).inserted_id
            mongo.db.categories.update_one(
                {"category_name": activity["category_name"]}, {"$push": {"activity_list": ObjectId(new_activity)}})
            flash("Activity added: {}".format(activity["activity_name"]))

            return redirect(url_for("get_activities"))


@app.route("/edit_activity/<activity_id>", methods=["GET", "POST"])
def edit_activity(activity_id):

    activity = mongo.db.activities.find_one({"_id": ObjectId(activity_id)})
    activity_owner = activity["created_by"]
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    current_category = mongo.db.categories.find_one({"category_name": activity["category_name"]})

    if "user" not in session:
        flash("You need to Log In to do that!")

        return redirect(url_for("login"))

    elif session["user"] != activity_owner and session["user"] != "admin":
        flash("This Activity belongs to someone else!")

        return redirect(url_for('view_activity', activity_id=ObjectId(activity_id)))

    elif request.method != "POST":
        return render_template(
            "edit_activity.html",
            activity=activity,
            categories=categories,
            ages=AGES)

    else:
        # if no new image chosen, keep existing image
        if request.files["image_file"].filename == "":
            edit_image_path = activity["image_file"]

        # otherwise prepare for uploading new image
        else:
            edit_image_path = upload_file()

        # get edit details
        edit = {"$set": {
            "activity_name": request.form.get("activity_name"),
            "category_name": request.form.get("category_name"),
            "target_age": request.form.get("target_age"),
            "activity_summary": request.form.get("activity_summary"),
            "activity_details": request.form.get("activity_details"),
            "activity_equipment": request.form.get("activity_equipment"),
            "image_file": edit_image_path,
        }}

        # create a list of activity names
        activities = list(mongo.db.activities.find())
        lowercase_name = request.form.get("activity_name").lower()
        lowercase_list = []
        for x in activities:
            lowercase_list.append(x["activity_name"].lower())

        # check whether name already taken
        if lowercase_name in lowercase_list:
            flash("'{}' already exists, please choose another name".format(request.form.get("activity_name")))

            return redirect(url_for('edit_activity', activity_id=ObjectId(activity_id)))

        else:
            # save activity edit details to database
            mongo.db.activities.update_many(activity, edit)

            # find the category chosen on form
            new_category = mongo.db.categories.find_one(
                {"category_name": request.form.get("category_name")})

            # if chosen category name is different from existing category name
            if request.form.get("category_name") != current_category["category_name"]:

                # move activity id from old activity_list to new one
                mongo.db.categories.update_one(
                    new_category,
                    {"$push": {"activity_list": activity["_id"]}})
                mongo.db.categories.update_one(
                    current_category,
                    {"$pull": {"activity_list": activity["_id"]}})

            flash("Activity updated ({})".format(activity["activity_name"]))

            return redirect(url_for('view_activity', activity_id=ObjectId(activity_id)))


@app.route("/delete_activity/<activity_id>")
def delete_activity(activity_id):

    activity = mongo.db.activities.find_one({"_id": ObjectId(activity_id)})
    activity_owner = activity["created_by"]

    if "user" not in session:
        flash("You need to Log In to do that!")

        return redirect(url_for("login"))

    elif session["user"] != activity_owner and session["user"] != "admin":
        flash("This Activity belongs to someone else!")

        return redirect(url_for('view_activity', activity_id=ObjectId(activity_id)))

    else:
        mongo.db.categories.find_one_and_update(
            {"category_name": activity["category_name"]},
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

    if "user" not in session:
        flash("You need to Log In to do that!")

        return redirect(url_for("login"))

    elif session["user"].lower() != "admin":
        flash("That's an Admin's job!")

        return redirect(url_for("get_categories"))

    elif request.method != "POST":
        return render_template("add_category.html")

    else:
        category = {
            "category_name": request.form.get("category_name"),
            "category_summary": request.form.get("category_summary"),
            "image_file": upload_file(),
            "activity_list": []
        }

        # create a list of category names
        categories = list(mongo.db.categories.find())
        lowercase_name = category["category_name"].lower()
        lowercase_list = []
        for x in categories:
            lowercase_list.append(x["category_name"].lower())

        # check whether name already taken
        if lowercase_name in lowercase_list:
            flash("'{}' already exists, please choose another name".format(category["category_name"]))

            return redirect(url_for('add_category'))

        mongo.db.categories.insert_one(category)
        flash("Category added ({})".format(category["category_name"]))

        return redirect(url_for("get_categories"))


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})

    if "user" not in session:
        flash("You need to Log In to do that!")

        return redirect(url_for("login"))

    elif session["user"].lower() != "admin":
        flash("That's an Admin's job!")

        return redirect(url_for("get_categories"))

    elif request.method != "POST":
        return render_template("edit_category.html", category=category)

    else:
        if request.files["image_file"].filename == "":
            edit_image_path = category["image_file"]

        else:
            edit_image_path = upload_file()

        edit = {"$set": {
            "category_summary": request.form.get("category_summary"),
            "image_file": edit_image_path,
        }}

        mongo.db.categories.update_many(category, edit)
        flash("Category updated ({})".format(category["category_name"]))

        return redirect(url_for("get_categories"))


@app.route("/delete_category/<category_id>")
def delete_category(category_id):

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    dependent_activities = list(mongo.db.activities.find(
        {"category_name": category["category_name"]}))
    unassigned_category = mongo.db.categories.find_one(
        {"category_name": "Unassigned"})
    activities = []

    if "user" not in session:
        flash("You need to Log In to do that!")

        return redirect(url_for("login"))

    elif session["user"].lower() != "admin":
        flash("That's an Admin's job!")

        return redirect(url_for("get_categories"))

    else:
        for activity in dependent_activities:
            mongo.db.activities.find_one_and_update(
                activity, {"$set": {"category_name": "Unassigned"}})
            activities.append(activity["_id"])

        mongo.db.categories.find_one_and_update(
            unassigned_category, {"$addToSet": {"activity_list": {"$each": activities}}})

        mongo.db.categories.remove(category)

        flash("Category deleted ({})".format(category["category_name"]))

        return redirect(url_for('get_categories'))


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html', error=error), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
