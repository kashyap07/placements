from flask import Flask, Blueprint, request, session, g, redirect, url_for, abort, render_template, flash
from .models import get_db

views = Blueprint('views', __name__);

@views.route("/")
def index():
	return render_template("index.html");

@views.route("/home")
@views.route("/overview")
def home():

	if not session.get('logged_in'):
		return redirect(url_for('views.login'));
	session['userprofile_pic'] = "/static/assets/images/rain-dp.jpg";
	return render_template("home.html")

@views.route('/signup', methods=['GET', 'POST'])
def signup():

	return render_template('home.html', error=error);

@views.route('/login', methods=['GET', 'POST'])
def login():
	print("hello")
	error = None
	db = get_db()
	if request.method == 'POST':
		print("hi", session.get('logged_in'))
		if not session.get('logged_in'):
			db = get_db()
			cur = db.execute('select * from Student where stud_id=(?);',[request.form['username'],])
			entries = cur.fetchall()
			print(entries)
			for entry in entries:
				if entry[9] == request.form['password']:
					session['logged_in'] = True
					flash('You were logged in')
					session['username']=request.form['username']
					return redirect(url_for('views.home'))
				else :
					return render_template('login.html', error="Invalid password")
			else :
				error = "Invalid username"

	if session.get('logged_in'):
		return redirect(url_for('views.home'));
	return render_template('login.html', error=error)

@views.route('/logout')
def logout():
	session.pop('logged_in', None)
	session.pop('username',None)
	flash('You were logged out')
	return redirect(url_for('views.login'))

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




@views.route('/x')
def x():
	return render_template('x.html');