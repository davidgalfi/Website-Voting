from flask import Blueprint, render_template
from model import Users, db

# Creating the admin blueprint
admin = Blueprint("admin", __name__, template_folder="templates", static_folder="static")


# Define the home route
@admin.route("/admin_home")
@admin.route("/")
def admin_home():
    return render_template("admin_home.html")


@admin.route("/users")
def users():
    all_user = Users.query.all()
    return render_template("admin_users.html", all_user=all_user)


@admin.route("/voting")
def vote():
    return render_template("admin_newvoting.html")
