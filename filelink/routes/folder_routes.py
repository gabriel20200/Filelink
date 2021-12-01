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
	FOLDER ROUTES
"""

# @ROUTE: New Folder Route
# @DESCRIPTION: Returns and creates new folders
@app.route('/folder/new', methods=["POST", "GET"])
def new_folder():
	if request.method == "POST":
		new_folder_name = request.form['folder_name_input']
		space_bar = " "

		if space_bar in new_folder_name:
			return redirect(
				url_for("new_folder")
			)

		elif len(new_folder_name) >= 21:
			return redirect(
				url_for("new_folder")
			)
		else:
			create_new_folder = FolderModel(folder_name=new_folder_name)
			db.session.add(create_new_folder)
			db.session.commit()

			print(f"{new_folder_name} has been created.")

			return redirect(
				url_for("index")
			)

	if request.method == "GET":
		return render_template(
			'new_folder.html',
			page_title="New Folder :: Filelink"
		)

# @ROUTE: Show Folder Route
# @DESCRIPTION: Finds the folder, and returns all the files that are within it.
@app.route('/folder/<selected_folder_name>', methods=["POST", "GET"])
def selected_folder(selected_folder_name):
	if request.method == "POST":
		file = request.files['file_upload']
		filename = secure_filename(file.filename)
		mimetype = file.mimetype
		folder_name = selected_folder_name

		new_file = FileStorage(
			file=file.read(),
			file_name=filename,
			file_mimetype=mimetype,
			folder_destination=folder_name
		)

		db.session.add(new_file)
		db.session.commit()

		return redirect(
			url_for('index')
		)

	if request.method == "GET":
		folder_name = selected_folder_name
		get_folder = FolderModel.query.filter_by(folder_name=folder_name).first()

		if not get_folder:
			return "Folder not found."

		elif get_folder:
			get_files = FileStorage.query.filter_by(folder_destination=folder_name).all()

			return render_template(
				'folder.html',
				page_title=f"{folder_name} :: Filelink",
				folder=get_folder,
				files=get_files
			)