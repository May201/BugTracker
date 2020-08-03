import os
from flask import Flask, render_template, redirect, request
from flask_pymongo import PyMongo
# from bson.objectid import ObjectId 


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'Bugtracker'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

db = PyMongo(app).db


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    return redirect("/dashboard")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")

    return redirect("/dashboard")


@app.route("/create-bug", methods=["GET", "POST"])
def create_bug():
    if request.method == "GET":
        return render_template("create-bug.html")
    else:
        # TODO: Save bug information to DB
        return redirect("/dashboard")


@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html", bugs=db.Issue_Log.find())


if __name__ == '__main__':
    app.run(
        host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True
    )
