
# [BugLogz](https://logz4bugz.herokuapp.com/)

This is a simple bug tracking application created using Python Flask framework. The application is designed to help a software development team share and manage bugs that have been discovered during testing

---

## User Stories
Below is the list of user stories for the bug tracking application

* ### Login
    This story is about the login flow for a user and the different stages involved.

    **Signup:**
    A new user can sign up for the application by entering an unique user email. The password does not have to be unique.

    **Screen Elements:** 
    There will be 2 input fields for entering the user email and password with a submit button to trigger validation of user input. For signup, the fields will be the same except for the submit button which will have a label of signup instead of submit

    **Validation:** 
    The user input will be validated on the backend

    **Successful login/signup:** 
    If the user inputs are correct, then the user will be redirected to the landing page

    **Error page:** 
    If the user inputs are incorrect, then the user will be redirected to the error page with an option to try again

* ### Dashboard
    The Dashboard is shown after the user login is successful. By default, this page displays in a table:
    * Bugs currently available
    * Bugs sorted by most recently updated ones

* ### Bug Creation
    This page provides a form to create a new bug by entering the following bug attributes:
    * Name
    * Description
    * Reported date 
    * Status 
    * Submit


* ### Bug Updates
    This page provides a form to update an existing bug by entering the following bug attributes:
    * Name
    * Description
    * Status

---

## Technologies Used
The project was created using the following technologies.


### Tools
* Gitpod is the IDE used for developing this project.
* PIP for installation of tools needed in this project.
* Git to handle version control.
* MongoDB Atlas is the database for this project
* GitHub to store and share all project code remotely.

### Libraries
* `jQuery` to simplify DOM manipulation.
* `Materialize` to simplify the structure of the website and make the website responsive easily.
* `Google Fonts` to style the website fonts.
* `PyMongo` to make communication between Python and MongoDB possible.
* `Flask` to construct and render pages.
* `Jinja2` to simplify displaying data from the backend of this project smoothly and effectively in html

### Languages
This project uses `HTML`, `CSS`, `JavaScript` and `Python` programming languages.

### Other Resources
* w3schools
* Stack Overflow
* Slack

---

## Deployment

This section deals with the deployment steps for different environments - local and heroku

### Running locally

To run this project in an IDE follow the instructions below:

Ensure you have the following tools: 
- An IDE such as [Gitpod](https://gitpod.io)

The following **must be installed** on your machine:
- [PIP](https://pip.pypa.io/en/stable/installing/)
- [Python 3](https://www.python.org/downloads/)
- [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03)
- An account at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) or MongoDB running locally on your machine. 


### Instructions
1. Save a copy of the github repository located [here](https://github.com/May201/BugTracker) by clicking the "download zip" button at the top of the page and extracting the zip file to your chosen folder. 
If you have Git installed on your system, you can clone the repository with the following command.
```bash
git clone https://github.com/May201/BugTracker
```

2. If possible open a terminal session in the unzip folder or `cd` to the correct location.


3. If needed, Upgrade pip locally with
```bash
pip install --upgrade pip.
```

4. Install all required modules with the command 
```bash
pip -r requirements.txt
```

5. Call the database `Bugtracker` with 2 collections called `Issue_Log` and `users`

6. You can now run the application with the command
```bash
python3 run.py
```

7. You can visit the website at `http://0.0.0.0:8080/`

### Heroku Deployment

To deploy BugTracker to heroku, take the following steps. If `requirements.txt` and `Procfile` are already available, skip the first 3 steps.

1. Create a `requirements.txt` file using the terminal command `pip freeze > requirements.txt`.

2. Create a `Procfile` with the terminal command 
```
echo "web: python app.py" > Procfile
```

3. `git add` and `git commit` the new requirements and Procfile and then `git push` the project to GitHub

4. Create a new app on the [Heroku website](https://dashboard.heroku.com/apps) by clicking the "New" button in your dashboard. Give it the name `logz4bugz` and set the region to `Europe`

5. From the heroku dashboard of the newly created application, click on "Deploy" > "Deployment method" and select GitHub

6. Confirm the linking of the heroku app to the correct GitHub repository

7. In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars"

8. Set the following config vars:

| Key | Value |
 --- | ---
DEBUG | FALSE
IP | 0.0.0.0
MONGO_URI | `mongodb+srv://<username>:<password>@cluster0-if9zz.mongodb.net/Bugtracker?retryWrites=true&w=majority`
PORT | 5000

- To get you MONGO_URI read the MongoDB Atlas documentation [here](https://docs.atlas.mongodb.com/)

9. In the heroku dashboard, click "Deploy".

10. In the "Manual Deployment" section of this page, make sure the `master` branch is selected and then click "Deploy Branch"

11. The site is now successfully deployed at `https://logz4bugz.herokuapp.com/`

---


