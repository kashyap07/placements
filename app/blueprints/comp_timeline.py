from flask import Flask, Blueprint, request, session, g, redirect, url_for, abort, render_template, flash
from .models import get_db, User, POfficer

comp_timeline = Blueprint('comp_timeline', __name__, static_url_path='/static');

@comp_timeline.route("/timeline")
def timeline():
    student_id = session['user']['username']
    company = get_db().execute(
        '''SELECT calendar.comp_id, company.comp_name, calendar.date, calendar.purpose
        FROM calendar,company
        where calendar.comp_id = company.comp_id
        ''').fetchall()
    print(company)
    registered = get_db().execute(
        '''SELECT comp_id
        FROM registered
        where registered.stud_id = ?
        ''',(student_id,)).fetchall()
    import datetime
    company = [list(x) for x in company]
    company = sorted(company,key=lambda x: datetime.datetime.strptime(x[2], '%d-%m-%Y').date())
    registered = [x[0] for x in registered]
    print(company)
    print(registered)
    return render_template("comp_timeline.html", companies=company, registered = registered)