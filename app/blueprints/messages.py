from flask import Flask, Blueprint, request, session, g, redirect, url_for, abort, render_template, flash
from .models import get_db, User, POfficer

messages = Blueprint('messages', __name__);



@messages.route('/history')
def history():
	db = get_db()
	cur = db.execute("SELECT * from postLog  where strftime('%d','now') - strftime('%d',LastPost) < 2 and stud_id =(?); ",[session.get('username'),])
	entries = cur.fetchall()
	return render_template('show_history.html',entries=entries)
	'''for entry in entries:
		print(entry[0],entry[1],entry[2],entry[3])
		sys.stdout.flush()	'''

@messages.route('/sendmessage',methods=['GET','POST'])
def sendmessage():
	
	if request.method == 'POST':
		print(" I am here in Post")
		sys.stdout.flush()
		if  session.get('logged_in'):
			print(" I am here session ")
			sys.stdout.flush()
			recipient = 'dishaatalreja@gmail.com'
			gmail_user = request.form['username']
			gmail_pwd = request.form['password']
			FROM = gmail_user
			TO = recipient if type(recipient) is list else [recipient]
			SUBJECT = request.form['subject']
			TEXT = request.form['body']
			message = """From: %s\nTo: %s\nSubject: %s\n\n%s""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
			try:
				server = smtplib.SMTP("smtp.gmail.com", 587)
				server.ehlo()
				server.starttls()
				server.login(gmail_user, gmail_pwd)
				server.sendmail(FROM, TO, message)
				server.close()
				db = get_db()
				cur = db.execute("INSERT into postLog(stud_id,Message) VALUES (?,?);",[session.get('username'),request.form['body']])
				db.commit()
				flash('successfully sent the mail')
				sys.stdout.flush()
			except:
				flash("failed to send mail")
				sys.stdout.flush()
	
	return render_template('send_message.html')
			