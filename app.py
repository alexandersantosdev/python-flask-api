from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import config, configure_db

app = Flask(__name__)

#Aplicaiton, Database and Marshmallow (serializer) configurations
config(app)
db = configure_db(app)
ma = Marshmallow(app)

#importing all te routes in routes module
from routes import *

#runs de app on http://localhost:5000
if __name__ == '__main__':
    app.run(debug=True)