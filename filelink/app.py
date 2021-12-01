#	Filelink - A homebrew file cloud storage.
#	@version 1.0.0
#	@authors Gabriel Gavrilov <gabrielgavrilov11@gmail.com>

"""
	SERVER IMPORTS
"""

import json
from flask import Flask, redirect, url_for, render_template, request, Response
from werkzeug.utils import secure_filename
from db_settings import db_init, db
from models import file_storage, folder

"""
	SERVER SETUP
"""

with open('./private constants.json') as jf:
	private_constants = json.load(jf)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = private_constants['SQLITE_URI']
# Disable this to not get any deprecated warnings
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.static_folder = './static'
db_init(app)

"""
	IMPORT WEB ROUTES
"""

from routes import index_routes
from routes import folder_routes
from routes import file_routes
from routes import delete_routes

"""
	RUN THE FLASK APPLICATION
"""

if __name__ == "__main__":
	app.run()