from flask import Flask, redirect, url_for, render_template, request
from datetime import timedelta
from views import views
from dotenv import load_dotenv
import os

app  = Flask(__name__)
app.register_blueprint(views, url_prefix="")

load_dotenv()
secret_key = os.getenv('SECRET_KEY')
app.secret_key = secret_key
app.permanent_session_lifetime = timedelta(minutes=5)

if __name__ == '__main__':
    app.run(debug=True, port=800)
