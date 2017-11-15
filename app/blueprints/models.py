"""
	module manages the database
"""
from flask import Flask, Blueprint, request, session, g, redirect, url_for, abort, render_template, flash, current_app
import sqlite3
import csv

models = Blueprint('models', __name__);
def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(current_app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
	if not hasattr(g, 'sqlite_db'):
		g.sqlite_db = connect_db()
	return g.sqlite_db

def init_db():
	db = get_db()
	with current_app.open_resource('db/schema.sql', mode='r') as f:
		db.cursor().executescript(f.read())
	db.commit()
	res = db.execute("SELECT name FROM sqlite_master WHERE type='table';")
	populate_db(current_app.root_path+"/db/")


def populate_db(path):
	db = get_db()
	with open(path+'Student.csv','rt') as fin:
		dr = csv.DictReader(fin)
		to_db = [(i['stud_id'], i['name'],i['cgpa'],i['sec_cgpa'],i['prim_cgpa'],i['contact'],i['email'],i['backlogs'],i['dept'],i['password']) for i in dr]
	db.executemany("INSERT INTO Student(stud_id,name,cgpa,sec_cgpa,prim_cgpa,contact,email,backlogs,dept,password) VALUES (?,?,?,?,?,?,?,?,?,?);", to_db)
	with open(path+'eligibility.csv','rt') as fin:
		dr = csv.DictReader(fin)
		to_db = [(i['comp_id'], i['dept'],i['cgpa'],i['backlogs'],i['internship'],i['sec_cgpa'],i['prim_cgpa']) for i in dr]
	db.executemany("INSERT INTO Eligibility(comp_id,dept,cgpa,backlogs,internship,sec_cgpa,prim_cgpa) VALUES (?,?,?,?,?,?,?);", to_db)
	
	with open(path+'job_info1.csv','rt') as fin:
		dr = csv.DictReader(fin)
		to_db = [(i['comp_id'], i['role'],i['ctc'],i['stipend'],i['location']) for i in dr]
	db.executemany("INSERT INTO Job_Info(comp_id,role,ctc,stipend,location) VALUES (?,?,?,?,?);", to_db)
	
	with open(path+'modeOfSelection.csv','rt') as fin:
		dr = csv.DictReader(fin)
		to_db = [(i['comp_id'], i['mode'],i['gd'],i['interview'],i['rounds']) for i in dr]
	db.executemany("INSERT INTO Mode_of_Selection(comp_id,mode,gd,interview,rounds) VALUES (?,?,?,?,?);", to_db)
	
	
	with open(path+'placed.csv','rt') as fin:
		dr = csv.DictReader(fin)
		to_db = [(i['stud_id'], i['comp_id'],i['ftjob'],i['internship'],i['role']) for i in dr]
	db.executemany("INSERT INTO Placed(stud_id,comp_id,ftjob,internship,role) VALUES (?,?,?,?,?);", to_db)
	
	with open(path+'calendar1.csv','rt') as fin:
		dr = csv.DictReader(fin)
		to_db = [(i['comp_id'], i['date'],i['purpose']) for i in dr]
	db.executemany("INSERT INTO Calendar(comp_id,date,purpose) VALUES (?,?,?);", to_db)
	
	
	#flash('Entry was successful')	
	
	db.commit()
	return ''