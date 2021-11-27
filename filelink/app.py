#	Filelink - A homebrew file cloud storage.
#	@version 1.0.0
#	@authors Gabriel Gavrilov <gabrielgavrilov11@gmail.com>

"""
	SERVER SETUP
"""

import json
from flask import Flask, redirect, url_for, render_template, request, Response
from werkzeug.utils import secure_filename
from db_settings import db_init, db
from db_models import FileStorage, FolderModel

with open('./private constants.json') as jf:
	private_constants = json.load(jf)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = private_constants['SQLITE_URI']
# Disable this to not get any deprecated warnings
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.static_folder = './static'
db_init(app)

"""
	WEB ROUTES
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

"""
	MISCELLANEOUS
"""

if __name__ == "__main__":
	app.run(debug=True)