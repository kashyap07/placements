#!/python3

import os
from flask import Flask, g
from werkzeug.utils import find_modules, import_string
#from placements.blueprints import #abc

def create_app(config=None):
	app = Flask(__name__);

	app.config.update(dict(
		#DATABASE=os.path.join(app.root_path, 'placements.db'),
		DEBUG=True,
		SECRET_KEY=b'_5#y2L"F4Q8z\n\xec]/',
		USERNAME='admin',
		PASSWORD='default'
	))
	app.config.update(config or {})
	app.config.from_envvar('PLACEMENT_SETTINGS', silent=True)
	register_blueprints(app)
	#register_cli(app)
	#register_teardowns(app)

	return app

def register_blueprints(app):
	for name in find_modules('app.blueprints'):
		mod = import_string(name)
		name = name.split(".")[-1]
		#name of the variable used to store the blueprint
		if hasattr(mod, name): 
			app.register_blueprint(getattr(mod, name))
	return None
"""
def registor_cli(app):
	@app.cli.command('initdb')
	def initdb_command():
		# Creates the database tables.
		init_db()
		print('Initialized the database.')

"""
app = create_app()
print(app.root_path, app.template_folder, app.url_map)