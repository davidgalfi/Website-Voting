from flask import Blueprint, render_template, request, redirect, url_for, session
from module import Users, db

# Creating the home blueprint
home = Blueprint("home", __name__, template_folder="templates", static_folder="static")

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin"


# Define the home route
@home.route("/main_home")
@home.route("/")
def main_home():
    return render_template("home.html", user_active=session.get("usr_active"))


@home.route("/login", methods=["POST", "GET"])
def login():
    if "usr_id" in session:
        session["usr_active"] = True
        return redirect(url_for("usr.user_home", user_id=session.get("usr_id")))

    if request.method == "POST":

        usr_name_get = request.form["usr_name"]
        usr_password_get = request.form["usr_password"]

        if ADMIN_USERNAME == usr_name_get and ADMIN_PASSWORD == usr_password_get:
            return redirect(url_for("admin.admin_home"))

        _usr = Users.query.filter_by(name=usr_name_get, password=usr_password_get).first()

        session["usr_name"] = _usr.name
        session["usr_password"] = _usr.password
        session["usr_email"] = _usr.email
        session["usr_id"] = _usr._id

        if _usr:
            session["usr_active"] = True
            return redirect(url_for("usr.user_home", user_id=_usr._id))
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

        found_user = Users.query.filter_by(name=usr_name).first()
        if found_user or ADMIN_USERNAME == usr_name:
            return redirect(url_for("home.register"))

        session["usr_name"] = usr_name
        session["usr_password"] = usr_password
        session["usr_email"] = usr_email

        db.session.add(Users(name=usr_name, password=usr_password, email=usr_email))
        db.session.commit()

        session["usr_id"] = Users.query.filter_by(email=usr_email).first()._id

        return redirect(url_for("home.login"))
    else:
        return render_template("register.html")


@home.route("/logout")
def logout():
    session.pop("usr_active", None)
    session.pop("usr_name", None)
    session.pop("usr_password", None)
    session.pop("usr_email", None)
    session.pop("usr_id", None)
    return redirect(url_for("home.main_home"))
