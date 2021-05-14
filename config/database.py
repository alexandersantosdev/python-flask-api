from flask_sqlalchemy import SQLAlchemy

def configure_db(app):
    db = SQLAlchemy(app)

    return db