from flask_sqlalchemy import SQLAlchemy
from main import app

db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


class Users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(100))
    email = db.Column("email", db.String(100))
    password = db.Column("password", db.String(16))
    vote_for = db.Column("vote", db.Integer)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


class Votes(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    vote_for = db.Column("vote", db.String(200))
    vote_choice_first = db.Column("first choice", db.StringU(100))
    vote_choice_second = db.Column("second choice", db.StringU(100))
    vote_choice_third = db.Column("third choice", db.StringU(100))

    def __init__(self, vote_for, vote_choice_first, vote_choice_second, vote_choice_third):
        self.vote_for = vote_for
        self.vote_choice_first = vote_choice_first
        self.vote_choice_second = vote_choice_second
        self.vote_choice_third = vote_choice_third
