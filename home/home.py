from flask import Blueprint, render_template

# Creating the home blueprint
home = Blueprint("home", __name__, template_folder="templates", static_folder="static")


# Define the home route
@home.route("/main_home")
@home.route("/")
def main_home():
    return render_template("home.html")
