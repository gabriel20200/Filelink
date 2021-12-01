from db_settings import db

# @MODEL: Folder Model
# @DESCRIPTION: Creates a folder dataset where the files are stored onto.
class FolderModel(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	folder_name = db.Column(db.Text, nullable=False)