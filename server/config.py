from flask import Flask
from numpy import unicode_
from routes import server_views
from flask_sqlalchemy import SQLAlchemy


server = Flask(__name__)

server.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


server.register_blueprint(server_views)
