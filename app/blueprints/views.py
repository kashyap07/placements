import os
from flask import Blueprint, render_template, g

views = Blueprint('views', __name__);

@views.route("/")
def index():
	return render_template("index.html");

@views.route("/home")
def home():
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

