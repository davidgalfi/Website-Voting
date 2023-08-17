from flask import Blueprint, render_template

# Creating the user blueprint
usr = Blueprint("usr", __name__, template_folder="templates")


# Define the home route
@usr.route("/main_home")
@usr.route("/")
def user_home():
    return render_template("user_home.html")
