import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date

if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


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
    if request.method == "POST":
        activity = {
            "activity_name": request.form.get("activity_name"),
            "category_name": request.form.get("category_name"),
            "age_name": request.form.get("age_name"),
            "activity_summary": request.form.get("activity_summary"),
            "activity_details": request.form.get("activity_details"),
            "created_by": session["user"],
            "date_added": date.today().strftime("%d %b %Y")
            # could use request.form.getlist for the equipment
        }
        cat_activities = mongo.db.categories.find_one(
            {"category_name": activity["category_name"]})["activity_count"]
        cat_activities_update = int(cat_activities + 1)

        mongo.db.categories.update_one(
            {"category_name": activity["category_name"]},
            {"$set": {"activity_count": cat_activities_update}})

        mongo.db.activities.insert_one(activity)
        flash("Activity Added")
        return redirect(url_for("get_activities"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    ages = mongo.db.ages.find()
    return render_template(
        "add_activity.html", categories=categories, ages=ages)


@app.route("/edit_activity/<activity_id>", methods=["GET", "POST"])
def edit_activity(activity_id):
    activity = mongo.db.activities.find_one({"_id": ObjectId(activity_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    ages = mongo.db.ages.find()

    if request.method == "POST":
        submit = {"$set": {
            "activity_name": request.form.get("activity_name"),
            "category_name": request.form.get("category_name"),
            "age_name": request.form.get("age_name"),
            "activity_summary": request.form.get("activity_summary"),
            "activity_details": request.form.get("activity_details"),
            "created_by": session["user"]
            # could use request.form.getlist for the equipment
        }}
        mongo.db.activities.update_many(activity, submit)
        flash("Activity Updated")
        return render_template("view_activity.html", activity=activity)

    return render_template(
        "edit_activity.html",
        activity=activity,
        categories=categories, ages=ages)


@app.route("/delete_activity/<activity_id>")
def delete_activity(activity_id):
    activity = mongo.db.activities.find_one({"_id": ObjectId(activity_id)})

    cat_activities = mongo.db.categories.find_one(
        {"category_name": activity["category_name"]})["activity_count"]
    cat_activities_update = int(cat_activities - 1)

    mongo.db.categories.update_one(
        {"category_name": activity["category_name"]},
        {"$set": {"activity_count": cat_activities_update}})

    mongo.db.activities.remove({"_id": ObjectId(activity_id)})

    flash("Activity Deleted")
    return redirect(url_for('profile', username=session['user']))


@app.route("/view_activity/<activity_id>")
def view_activity(activity_id):
    activity = mongo.db.activities.find_one({"_id": ObjectId(activity_id)})
    return render_template("view_activity.html", activity=activity)


@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find())
    return render_template("categories.html", categories=categories)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
