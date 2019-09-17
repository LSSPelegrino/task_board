"""
Initialize App Module
"""

# # 3rd Party Modules
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# # Internal Modules
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# # Recursive Imports
from app import app, models, routes
