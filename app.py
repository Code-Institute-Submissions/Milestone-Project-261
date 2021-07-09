import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
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
    # list all cryptos
    cryptos = list(cryptos_coll.find())
    # show watched cryptos
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


@app.route("/search", methods=["GET", "POST"])
def search():
    # search query in cryptos collection
    query = request.form.get("query")
    cryptos = list(mongo.db.cryptos.find({"$text": {"$search": query}}))
    # show watched cryptos
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
    # get user watchlist
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


@app.route("/add_watchlist/<crypto_id>/<url>")
def add_watchlist(crypto_id, url):
    # add to user watchlist
    if "user" in session:
        users_coll.find_one_and_update(
            {"username": session["user"]},
            {"$push": {"watched_cryptos": ObjectId(crypto_id)}})
        if url == "index":
            return redirect(url_for("index"))
        else:
            return redirect(url_for("get_crypto",
                                    crypto_id=crypto_id))


@app.route("/remove_watchlist/<crypto_id>/<url>")
def remove_watchlist(crypto_id, url):
    # remove from user watchlist
    if "user" in session:
        username = users_coll.find_one(
            {"username": session["user"]})["username"]
        users_coll.find_one_and_update(
            {"username": session["user"]},
            {"$pull": {"watched_cryptos": ObjectId(crypto_id)}})
        if url == "index":
            return redirect(url_for("index"))
        elif url == "watchlist":
            return redirect(url_for("watchlist", username=username))
        else:
            return redirect(url_for("get_crypto",
                                    crypto_id=crypto_id))


@app.route("/get_crypto/<crypto_id>")
def get_crypto(crypto_id):
    # get the crypto using the crypto id
    crypto = cryptos_coll.find_one({"_id": ObjectId(crypto_id)})
    comments = []
    # loop through the crypto comments
    for comment in crypto["comments"]:
        crypto_comments = comments_coll.find_one({"_id": ObjectId(comment)})
        comments.append(crypto_comments)
    # find if crypto is apart of watchlist
    if 'user' in session:
        username = users_coll.find_one(
            {"username": session["user"]})
        watched_cryptos = username["watched_cryptos"]
        return render_template("crypto.html",
                               crypto=crypto,
                               watched_cryptos=watched_cryptos,
                               comments=comments)
    else:
        return render_template("crypto.html",
                               crypto=crypto,
                               comments=comments)


@app.route("/add_comment/<crypto_id>", methods=["POST"])
def add_comment(crypto_id):
    # add comment to the crypto page
    if "user" in session:
        # https://www.programiz.com/python-programming/datetime/strftime
        date_added = datetime.today().strftime("%d/%m/%Y, %H:%M")
        new_comment = {
            "username": session["user"],
            "comment_date": date_added,
            "comment": request.form.get("crypto-comment")
        }
        # add comment to the comments collection
        insert_comment = comments_coll.insert_one(new_comment)
        # add comment to the crypto's comments array
        cryptos_coll.update_one({"_id": ObjectId(crypto_id)},
                               {"$push":
                                   {"comments":
                                       {"$each": [insert_comment.inserted_id],
                                        "$position": 0
                                        }
                                    }
                                }
                               )
        flash("Thank you for commenting")
        return redirect(url_for("get_crypto",
                                crypto_id=crypto_id))
    else:
        return redirect(url_for("get_crypto",
                                crypto_id=crypto_id))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
