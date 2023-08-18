from flask import Flask, redirect, url_for, render_template
from user.user import usr
from home.home import home
from admin.admin import admin

# Create the Flask web framework by create a Flask instance
app = Flask(__name__)

# Register blueprints
app.register_blueprint(usr, url_prefix="/user")
app.register_blueprint(home, url_prefix="/home")
app.register_blueprint(admin, url_prefix="/admin")
app.secret_key = "#123&321#"

# Main route redirect to the home page
@app.route("/")
def home():
    return "Home"


# Starting the server
if __name__ == "__main__":
    app.run(debug=True)
