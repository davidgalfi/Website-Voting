from flask import Blueprint, render_template

# Creating the admin blueprint
admin = Blueprint("admin", __name__, template_folder="templates", static_folder="static")


# Define the home route
@admin.route("/admin_home")
@admin.route("/")
def admin_home():
    return render_template("admin_home.html")
