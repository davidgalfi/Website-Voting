from flask import Blueprint, render_template, request, redirect, url_for, session

# Creating the home blueprint
home = Blueprint("home", __name__, template_folder="templates", static_folder="static")


# Define the home route
@home.route("/main_home")
@home.route("/")
def main_home():
    return render_template("home.html")


@home.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        usr_name_get = request.form["usr_name"]
        usr_password_get = request.form["usr_password"]

        usr_name = session.get("usr_name")
        usr_password = session.get("usr_password")

        print(usr_name)
        print(usr_password)
        print(usr_name_get)
        print(usr_password_get)

        if usr_name == usr_name_get and usr_password == usr_password_get:
            return redirect(url_for("usr.user_home", username=usr_name))
        else:
            return render_template("login.html")
    else:
        return render_template("login.html")


@home.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        usr_name = request.form["usr_name"]
        usr_password = request.form["usr_password"]
        usr_email = request.form["usr_email"]

        session["usr_name"] = usr_name
        session["usr_password"] = usr_password
        session["usr_email"] = usr_email

        return redirect(url_for("home.login", user=usr_name))
    else:
        return render_template("register.html")
