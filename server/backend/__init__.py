# from backend.views import serverViews
from flask import Flask
from backend.routes.server_views import server_views

server = Flask(__name__)

server.register_blueprint(server_views)
