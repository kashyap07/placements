from flask import Flask, Blueprint, request, session, g, redirect, url_for, abort, render_template, flash
from .models import get_db, User, POfficer

views = Blueprint('views', __name__);

@views.route("/")
def index():
	return render_template("index.html");

@views.route("/home")
def home():
	if not session.get('logged_in'):
		return redirect(url_for('views.login'));
	session['userprofile_pic'] = "/static/assets/images/rain-dp.jpg";
	return render_template("notifications.html")

@views.route('/signup', methods=['GET', 'POST'])
def signup():
	db = get_db()
	message = None
	if request.method == "POST" and not session.get('logged_in'):
		cur = db.execute('select * from Student where stud_id=(?) or email=(?);',[request.form['username'], request.form['email']])
		entries = cur.fetchall()
		if len(entries) > 0:
			message = "username or Email id already registered"
		else:
			data = request.form
			print(data)
			to_db = [data['username'], data['name'], data['cgpa'], data['sec_cgpa'], data['prim_cgpa'], data['contact'], data['email'], data['backlogs'], data['dept'], data['password']]
			print("new_1")
			db.execute("INSERT INTO Student(stud_id,name,cgpa,sec_cgpa,prim_cgpa,contact,email,backlogs,dept,password) VALUES (?,?,?,?,?,?,?,?,?,?);",tuple(to_db))
			db.commit();
			session['logged_in'] = True
			flash('You were signed up')
			session['user'] = User(to_db[:-1]).__dict__
			return render_template('home.html', message="You have successfully signed up.")

	if session.get('logged_in'):
		return redirect(url_for('views.home'));

	return render_template('signup.html', message=message);

@views.route('/login', methods=['GET', 'POST'])
def login():
	message = None
	db = get_db()
	if request.method == 'POST' and not session.get('logged_in'):
		db = get_db()
		cur = db.execute('select * from Student where stud_id=(?);',[request.form['username'],])
		entries = cur.fetchall()
		for entry in entries:
			if entry[9] == request.form['password']:
				session['logged_in'] = True
				flash('You were logged in')
				session['user']= User(list(entry)[:-1]).__dict__
				return redirect(url_for('views.home'))
			else :
				return render_template('login.html', message="Invalid password")
		else :
			error = "Invalid username"

	if session.get('logged_in'):
		return redirect(url_for('views.home'));
	return render_template('login.html', message=message)

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