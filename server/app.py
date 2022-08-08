from models import database
from config import server
from flask_migrate import Migrate

migrate = Migrate(server, database)
