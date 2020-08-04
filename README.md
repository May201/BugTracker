
# BugLogz

This is a simple bug tracking application created using Python Flask frame work. The application is designed to help a software development team share and manage bugs that have been discovered.



## User Stories
Below is the list of user stories for the bug tracking application
### Login
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

### Dashboard
The Dashboard is shown after the user login is successful. By default, this page displays in a table:
* Bugs currently available
* Bugs sorted by most recently updated ones

### Bug Creation
This page provides a form to create a new bug by entering the following bug attributes:
* Name
* Description
* Reported date 
* Status 
* Submit


### Bug Updates
This page provides a form to update an existing bug by entering the following bug attributes:
* Name
* Description
* Status


## Technologies Used
The project was created using the following technologies.


### Tools
* Gitpod is the IDE used for developing this project.
* PIP for installation of tools needed in this project.
* Git to handle version control.
* MongoDB Atlas is the database for this project
* GitHub to store and share all project code remotely.

### Libraries
* JQuery to simplify DOM manipulation.
* Materialize to simplify the structure of the website and make the website responsive easily.
* Google Fonts to style the website fonts.
* PyMongo to make communication between Python and MongoDB possible.
* Flask to construct and render pages.
* Jinja to simplify displaying data from the backend of this project smoothly and effectively in html

### Languages
This project uses HTML, CSS, JavaScript and Python programming languages.

### Other Resources
* w3schools
* Stack Overflow
* Slack

--------


