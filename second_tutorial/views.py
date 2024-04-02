from flask import Blueprint, redirect, url_for, render_template, request, decorator

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html")

@views.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("login.html")

@views.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"
