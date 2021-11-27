from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Sets up the database
def db_init(app):
	db.init_app(app)

	with app.app_context():
		db.create_all()