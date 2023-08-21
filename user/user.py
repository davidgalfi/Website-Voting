from flask import Blueprint, render_template, request
from module import Users, db

# Creating the user blueprint
usr = Blueprint("usr", __name__, template_folder="templates", static_folder="static")


# Define the user_home route
@usr.route("/user_home")
@usr.route("/")
def user_home():
    user_id = request.args.get("user_id")
    user = Users.query.get(user_id)
    return render_template("user_home.html", username=user.name)
