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
	FILE ROUTES
"""

# @ROUTE: File Route
# @DESCRIPTION: Finds and returns the selected file. 
@app.route('/folder/<selected_folder_name>/file/<id>', methods=["POST", "GET"])
def response(selected_folder_name, id):
	if request.method == "POST":
		pass

	if request.method == "GET":
		folder_name = selected_folder_name
		file_id = id

		get_folder = FolderModel.query.filter_by(folder_name=folder_name).first()

		if not get_folder:
			return "Folder not found"

		elif get_folder:
			get_file = FileStorage.query.filter_by(id=file_id).first()
			return Response(
				get_file.file,
				mimetype=get_file.file_mimetype
			)