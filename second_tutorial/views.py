from flask import Blueprint, redirect, url_for, render_template, request, session, flash

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
        flash("Login Successful!")
        return redirect(url_for("views.user"))
    else:
        if "user" in session and session["user"] != '':
            flash("Already Logged In!")
            return redirect(url_for("views.user"))
        return render_template("login.html")

@views.route("/user", methods=["POST", "GET"])
def user():
    email = None
    if "user" in session and session["user"] != "":
        user = session["user"]
        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            flash("Email was saved!")
        else:
            if "email" in session:
                email = session["email"]
        return render_template("user.html", email=email)
    else:
        flash("You are not logged in!")
        return redirect(url_for("views.login"))

@views.route("/logout")
def logout():
    if "user" in session and session["user"] != "":
        user = session["user"]
        flash(f"{user} has logged out.", "info")
    session.pop("user", None)
    session.pop("email", None)
    return redirect(url_for("views.login"))
