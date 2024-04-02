from flask import Blueprint, redirect, url_for, render_template, request, session

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html")

@views.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("views.user"))
    else:
        if "user" in session and session["user"] != '':
            return redirect(url_for("views.user"))
        return render_template("login.html")

@views.route("/user")
def user():
    if "user" in session and session["user"] != "":
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("views.login"))

@views.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("views.login"))
