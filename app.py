import os
from flask import Flask, render_template, redirect, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


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
        db.Issue_Log.insert_one(request.form.to_dict())
        return redirect("/dashboard")


@app.route('/edit_task/<task_id>')
def edit_task(task_id):
    # the_task =  mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    # all_categories =  mongo.db.categories.find()
    # return render_template('edittask.html', task=the_task,
    #                        categories=all_categories)
    return redirect("/dashboard")


@app.route('/mark_complete/<task_id>')
def mark_complete(task_id):
    db.Issue_Log.update(
        {'_id': ObjectId(task_id)},
        {
            '$set': {
                'status': 'Completed'
            }
        }
    )
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
