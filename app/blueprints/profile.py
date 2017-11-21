from flask import Flask, Blueprint, request, session, g, redirect, url_for, abort, render_template, flash
from .models import get_db, User, POfficer
from .views import views

profile = Blueprint('profile', __name__, template_folder="/template");



@profile.route("/edit")
def profile_edit():
	if session.get('logged_in'):
		return render_template('profile_edit.html')
	return redirect(url_for('views.index'))

@profile.route("/save", methods=['GET', 'POST'])
def profile_save():
	if request.method == 'POST' and session.get('logged_in'):
		print("hi")
		db = get_db()
		data = request.form
		to_db = [data['name'], data['cgpa'], data['sec_cgpa'], data['prim_cgpa'], data['contact'], data['email'], data['backlogs'], data['dept']]
		print(session['user'])
		cur = db.execute('select * from Student where stud_id=(?);',[session['user']['username']])
		entry = cur.fetchall()[0]
		to_db = [entry[0]] + to_db + [entry[9]]
		db.execute('DELETE FROM Student where stud_id=(?)', [entry[0]])
		db.execute("INSERT INTO Student(stud_id,name,cgpa,sec_cgpa,prim_cgpa,contact,email,backlogs,dept,password) VALUES (?,?,?,?,?,?,?,?,?,?);",tuple(to_db))
		db.commit();
		session['user'] = User(to_db).__dict__
		return redirect(url_for('views.profile'));
	return redirect(url_for('views.index'));

@profile.route("/change", methods=['GET', 'POST'])
def change_password():
	if request.method == 'POST' and session.get('logged_in'):
		db = get_db()
		data = session['user']
		opasswd = request.form['opasswd']
		npasswd = request.form['npasswd']
		to_db = [data['username'], data['name'], data['cgpa'], data['sec_cgpa'], data['prim_cgpa'], data['contact'], data['email'], data['backlogs'], data['dept']]
		cur = db.execute('select * from Student where stud_id=(?);',[session['user']['username']])
		entry = cur.fetchall()[0]
		type(entry)
		if opasswd == entry[9]:
			to_db.append(npasswd)
			db.execute('DELETE FROM Student where stud_id=(?)', [entry[0]])
			db.execute("INSERT INTO Student(stud_id,name,cgpa,sec_cgpa,prim_cgpa,contact,email,backlogs,dept,password) VALUES (?,?,?,?,?,?,?,?,?,?);",tuple(to_db))
			db.commit()
			session['user'] = User(to_db).__dict__
		else:
			return redirect(url_for('views.profile'))

	return redirect(url_for('views.profile'))