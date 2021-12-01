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
	DELETE ROUTES
"""

# @ROUTE: Delete Folder Route
# @DESCRIPTION: Finds all the files inside the folder and deleted them. Once all the files are deleted, the folder will be deleted.
@app.route('/folder/delete/<selected_folder_name>', methods=["POST", "GET"])
def delete_folder(selected_folder_name):
	if request.method == "POST":
		pass

	if request.method == "GET":
		folder_name = selected_folder_name

		get_folder = FolderModel.query.filter_by(folder_name=folder_name).first()

		if not get_folder:
			return "Folder not found"

		elif get_folder:
			get_all_files = FileStorage.query.filter_by(folder_destination=folder_name).all()

			for file in get_all_files:
				db.session.delete(file)
				db.session.commit()

			db.session.delete(get_folder)
			db.session.commit()

			return redirect(
				url_for("index")
			)

# @ROUTE: Delete File Route
# @DESCRIPTION: Deletes the selected file from the database.
@app.route('/folder/<selected_folder_name>/delete/<id>', methods=["POST", "GET"])
def delete_file(selected_folder_name, id):
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
			db.session.delete(get_file)
			db.session.commit()

			return redirect(
				url_for("index")
			)
