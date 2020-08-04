import os
from flask import Flask, render_template, redirect, request, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


# Flask application initialization
app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'Bugtracker'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')
app.secret_key = os.urandom(24)

# Shortcut to the database
db = PyMongo(app).db


@app.route("/login", methods=["GET", "POST"])
def login():
    # Displaying the login page
    if request.method == "GET":
        return render_template("login.html")

    # Check login details and then redirect to dashboard
    user_email = request.form.get('email')
    existing_user = db.users.find_one({'email': user_email})
    if existing_user is None:
        return render_template("login.html", error=True)

    session['user_email'] = user_email
    return redirect("/dashboard")


@app.route("/logout")
def logout():
    # Reset the user email in the session
    session['user_email'] = ''
    return redirect("/login")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    # Display the signup page
    if request.method == "GET":
        return render_template("signup.html")

    # On successfull signup, redirect to dashboard
    user_email = request.form.get('email')
    existing_user = db.users.find_one({'email': user_email})
    if existing_user is None:
        db.users.insert_one(request.form.to_dict())
    else:
        return render_template("signup.html", error=True)

    session['user_email'] = user_email
    return redirect("/dashboard")


@app.route("/create-bug", methods=["GET", "POST"])
def create_bug():
    if request.method == "GET":
        # Display the create bug page
        return render_template("create-bug.html")
    else:
        # Insert the new bug details into the database
        db.Issue_Log.insert_one(request.form.to_dict())
        return redirect("/dashboard")


@app.route('/edit-bug/<bug_id>', methods=['GET', 'POST'])
def edit_bug(bug_id):
    if request.method == 'GET':
        # Find the bug details and then populate the Edit Bug page
        the_bug = db.Issue_Log.find_one({"_id": ObjectId(bug_id)})
        return render_template('edit-bug.html', bug=the_bug)
    else:
        # Update the bug details in the database
        # Redirect to the dashboard so that the latest list of bugs are shown
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
    # One-click action to change the status of a bug to completed
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
    # Common URL to load the dashboard
    return render_template(
        "dashboard.html",
        bugs=db.Issue_Log.find().sort('_id', -1)
    )


if __name__ == '__main__':
    # Start the web application
    app.run(
        host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True
    )
