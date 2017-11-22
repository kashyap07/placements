from flask import Flask, Blueprint, request, session, g, redirect, url_for, abort, render_template, flash
from .models import get_db, User, POfficer

notification = Blueprint('notification', __name__);


@notification.route('/register/<comp_name>/')
def register(comp_name):
	print(comp_name)
	sys.stdout.flush()
	db = get_db()
	cur = db.execute('select * from Student where stud_id=(?);',[session.get('username'),])
	print("I am here")
	sys.stdout.flush()
	entries = cur.fetchall()
	f = open(comp_name+'.csv','r')
	line_no = 0
	registered = []
	for line in f:
		if line_no == 0:
			line_no = line_no+1
			continue
		registered.append(line.split(',')[0].strip())
		
	f.close()
	#print(registered)
	with open(comp_name+'.csv','a') as out:
		csv_out=csv.writer(out)
		for entry in entries :
			#csv_out.writerow(entry)
			l = []
			if entry[0] in registered:
				flash('You have already registered')
				return redirect(url_for('notifications'))
			else :
				for e in entry:
					l.append(e)
				print(tuple(l))
				csv_out.writerow(tuple(l))
				sys.stdout.flush()
			out.close()
	flash("you have successfully registred")
	return redirect(url_for('notifications'))

@notification.route('/information/<comp_name>/')
def information(comp_name):
	db = get_db()
	cur = db.execute('select c.comp_id,c.comp_name,c.address,c.description,c.sector,c.tier,c.contact,j.role,j.ctc,j.stipend,j.location from Company c,Job_Info j where c.comp_name=(?) and c.comp_id=j.comp_id;',[comp_name,])
	entries = cur.fetchall()
	return render_template('show_company_info.html', entries=entries)	


