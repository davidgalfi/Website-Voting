from flask import Blueprint, render_template

# Creating the user blueprint
usr = Blueprint("usr", __name__, template_folder="templates", static_folder="static")


# Define the user_home route
@usr.route("/user_home/<username>/<password>/<email>")
@usr.route("/<username>")
def user_home(username, password, email):
    return render_template("user_home.html", username=username, password=password, email=email)
