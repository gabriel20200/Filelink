"""
	SERVER IMPORTS
"""

import json
from app import app, redirect, url_for, render_template, request, Response
from werkzeug.utils import secure_filename
from db_settings import db_init, db
from models import file_storage, folder

# Creates the database model variables
FolderModel = folder.FolderModel
FileStorage = file_storage.FileStorage

"""
	INDEX ROUTES
"""

# @ROUTE: Index Route
# @DESCRIPTION: Returns the index page
@app.route('/', methods=["POST", "GET"])
def index():
	if request.method == "POST":
		pass

	if request.method == "GET":
		get_folders = FolderModel.query.all()

		return render_template(
			'index.html',
			page_title="Folders :: Filelink",
			folders=get_folders
		)