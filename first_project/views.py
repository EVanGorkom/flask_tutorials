from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html", name="Ethan")

# Passing in data through the url and query parameters 
@views.route("/profile")
def profile():
    # args = request.args
    # name = args.get('name')
    # return render_template("index.html", name=name)
    return render_template("profile.html")

# Displaying json data
@views.route("/json")
def get_json():
    return jsonify({'name': 'ethan', 'coolness': 10})

# Receiving json data
@views.route("/data")
def get_data():
    data = request.data
    return jsonify(data)

# Redirect
@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.home"))