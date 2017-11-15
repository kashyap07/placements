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
	print("Successfully populated the db.",[ x[0] for x in res])
