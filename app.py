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
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024

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
    """
    We check the request.files object for a activity_image key.
    (activity_image is the name of the file input in add_activity and edit_activity)
    If it's not there, we return blank output
    """
    output = ""
    if "activity_image" not in request.files:
        return output

    # If the key is in the object, we save it in a variable called file
    file = request.files["activity_image"]

    """
    We check the filename attribute on the object
    If empty, it means the user sumbmitted an empty form, so we return a blank output
    """

    if file.filename == "":
        return output

    """Check that there is a file and that it has an allowed filetype
    https://flask.palletsprojects.com/en/master/patterns/fileuploads/
    """

    if file and allowed_file(file.filename):
        file.filename = secure_filename(file.filename)
        output = upload_file_to_s3(file)
    return output


def upload_file_to_s3(file):

    """
    Docs: http://boto3.readthedocs.io/en/latest/guide/s3.html
    """

    try:
        s3.upload_fileobj(file, S3_BUCKET, file.filename, ExtraArgs={
            "ACL": "public-read", "ContentType": file.content_type}
        )

    except Exception as e:
        print("Something Happened: ", e)
        return e

    return "{}{}".format(S3_LOCATION, file.filename)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/get_activities")
def get_activities():
    activities = mongo.db.activities.find().sort("_id", -1)
    categories = list(mongo.db.categories.find())

    return render_template(
        "activities.html", activities=activities, categories=categories)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
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
                flash("Welcome, {}".format(request.form.get("username")))
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
        {"created_by": session["user"]}))
    categories = list(mongo.db.categories.find())

    if session["user"]:
        return render_template(
            "profile.html", username=username,
            activities=activities, categories=categories)

    return redirect(url_for("get_activities"))


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_activity", methods=["GET", "POST"])
def add_activity():
    ages = ["Under 2", "2-4", "4-6", "6+"]
    categories = mongo.db.categories.find().sort("category_name", 1)
    image_path = upload_file()

    if request.method == "POST":
        activity = {
            "activity_name": request.form.get("activity_name"),
            "category_name": request.form.get("category_name"),
            "target_age": request.form.get("target_age"),
            "activity_summary": request.form.get("activity_summary"),
            "activity_details": request.form.get("activity_details"),
            "activity_equipment": request.form.get("activity_equipment"),
            "activity_image": image_path,
            "created_by": session["user"],
            "date_added": date.today().strftime("%d %b %Y")
        }
        mongo.db.categories.update_one(
            {"category_name": activity["category_name"]},
            {"$push": {"activity_list": activity["activity_name"]}})

        mongo.db.activities.insert_one(activity)
        flash("Activity Added")
        return redirect(url_for("get_activities"))

    return render_template(
        "add_activity.html", categories=categories, ages=ages)


@app.route("/edit_activity/<activity_id>", methods=["GET", "POST"])
def edit_activity(activity_id):
    activity = mongo.db.activities.find_one({"_id": ObjectId(activity_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    ages = ["Under 2", "2-4", "4-6", "6+"]
    edit_image_path = upload_file()

    current_category = mongo.db.categories.find_one({"category_name": activity["category_name"]})

    if request.method == "POST":
        submit = {"$set": {
            "activity_name": request.form.get("activity_name"),
            "category_name": request.form.get("category_name"),
            "target_age": request.form.get("target_age"),
            "activity_summary": request.form.get("activity_summary"),
            "activity_details": request.form.get("activity_details"),
            "activity_equipment": request.form.get("activity_equipment"),
            "activity_image": edit_image_path,
            "created_by": session["user"]
        }}
        mongo.db.activities.update_many(activity, submit)
        new_category = mongo.db.categories.find_one(
                {"category_name": request.form.get("category_name")})

        if request.form.get("category_name") != current_category["category_name"]:
            mongo.db.categories.update_one(
                new_category,
                {"$push": {"activity_list": activity["activity_name"]}})
            mongo.db.categories.update_one(
                current_category,
                {"$pull": {"activity_list": activity["activity_name"]}})

        flash("Activity Updated")
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
        {"$pull": {"activity_list": activity["activity_name"]}})

    mongo.db.activities.remove({"_id": ObjectId(activity_id)})

    flash("Activity Deleted")
    return redirect(url_for('profile', username=session['user']))


@app.route("/view_activity/<activity_id>")
def view_activity(activity_id):
    activity = mongo.db.activities.find_one({"_id": ObjectId(activity_id)})
    return render_template("view_activity.html", activity=activity)


@app.route("/get_categories")
def get_categories():
    activities = list(mongo.db.activities.find())
    categories = list(mongo.db.categories.find())
    return render_template("categories.html", categories=categories, activities=activities)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name"),
            "category_summary": request.form.get("category_summary"),
            "category_image": request.form.get("category_image"),
            "activity_list": []
        }

        mongo.db.categories.insert_one(category)
        flash("Category Added")
        return redirect(url_for("get_categories"))

    return render_template(
        "add_category.html")


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    categories = mongo.db.categories.find()
    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})

    if request.method == "POST":
        submit = {"$set": {
            "category_summary": request.form.get("category_summary"),
            "category_image": request.form.get("category_image"),
        }}
        mongo.db.categories.update_many(category, submit)
        flash("Category Updated")
        return render_template("categories.html", categories=categories)

    return render_template(
        "edit_category.html", category=category)


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    mongo.db.categories.remove(category)

    flash("Category Deleted")
    return redirect(url_for('get_categories'))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
