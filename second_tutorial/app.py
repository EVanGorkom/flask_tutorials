from flask import Flask, redirect, url_for, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
from views import views
from dotenv import load_dotenv
import os

app  = Flask(__name__)
app.register_blueprint(views, url_prefix="")

load_dotenv()
secret_key = os.getenv('SECRET_KEY')
app.secret_key = secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.permanent_session_lifetime = timedelta(minutes=5)

db = SQLAlchemy(app)

class Users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(100))
    email = db.Column("email", db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=800)
