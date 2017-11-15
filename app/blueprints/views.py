import os
from flask import Blueprint, render_template, g, session

views = Blueprint('views', __name__);

@views.route("/")
def index():
	return render_template("index.html");

@views.route("/home")
def home():
	session['username'] = "John Doe"
	return render_template("home.html", user="John Doe")

@views.route("/login")
def login():
	return render_template("login.html");

@views.route("/profile")
def profile():
	return render_template("profile.html")

@views.route("/notifications")
def notifications():
	return render_template("notifications.html")


@views.route("/messages")
def messages():
	return render_template("messages.html")


@views.route("/comp_timeline")
def comp_timeline():
	return render_template("comp_timeline.html")



