from flask import Blueprint, render_template

# Creating the home blueprint
home = Blueprint("home", __name__, template_folder="templates", static_folder="static")


# Define the home route
@home.route("/main_home")
@home.route("/")
def main_home():
    return render_template("home.html")


@home.route("/login")
def login():
    return render_template("login.html")

@home.route("/register")
def register():
    return render_template("register.html")
