import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

cryptos_coll = mongo.db.cryptos
users_coll = mongo.db.users
comments_coll = mongo.db.comments


@app.route("/")
@app.route("/index")
def index():
    cryptos = cryptos_coll.find()
    if 'user' in session:
        username = users_coll.find_one(
            {"username": session["user"]})
        watched_cryptos = username["watched_cryptos"]
        return render_template("index.html",
                               cryptos=cryptos,
                               watched_cryptos=watched_cryptos)
    else:
        return render_template("index.html",
                               cryptos=cryptos)


@app.route("/register", methods=["GET", "POST"])
def register():
    # registers a new user
    if request.method == "POST":
        existing_user = users_coll.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("You are already registered!")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "watched_cryptos": []
        }

        users_coll.insert_one(register)
        session["user"] = request.form.get("username").lower()
        flash("Registration successful!")
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = users_coll.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(request.form.get("username")))
                    return redirect(url_for(
                    "index", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/watchlist")
def watchlist():
    if "user" in session:
        username = users_coll.find_one(
            {"username": session["user"]})
        watched_cryptos = []
        for crypto in username["watched_cryptos"]:
            watched_cryptos_list = cryptos_coll.find_one({
                "_id": ObjectId(crypto)})
            watched_cryptos.append(watched_cryptos_list)
        if session["user"]:
            return render_template("watchlist.html",
                                   username=username,
                                   watched_cryptos=watched_cryptos)
    else:
        return redirect(url_for("watchlist.html"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)