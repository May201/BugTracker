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


@app.route('/edit-bug/<bug_id>', methods=['GET', 'POST'])
def edit_bug(bug_id):
    if request.method == 'GET':
        the_bug = db.Issue_Log.find_one({"_id": ObjectId(bug_id)})
        return render_template('edit-bug.html', bug=the_bug)
    else:
        db.Issue_Log.update(
            {'_id': ObjectId(bug_id)},
            {
                '$set': {
                    'title': request.form.get('title'),
                    'desc': request.form.get('desc'),
                    'priority': request.form.get('priority'),
                    'modified': request.form.get('modified')
                }
            }
        )
        return redirect('/dashboard')


@app.route('/mark_complete/<bug_id>')
def mark_complete(bug_id):
    db.Issue_Log.update(
        {'_id': ObjectId(bug_id)},
        {
            '$set': {
                'status': 'Completed'  # Update only specific field
            }
        }
    )
    return redirect("/dashboard")


@app.route('/dashboard')
def dashboard():
    return render_template(
        "dashboard.html",
        bugs=db.Issue_Log.find().sort('_id', -1)
    )


if __name__ == '__main__':
    app.run(
        host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True
    )
