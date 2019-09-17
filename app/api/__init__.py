"""
Initialize Api Module
"""

# # 3rd Party Imports
from flask_restful import Api

# # Internal Imports
from app import app

api = Api(app)


# # Recursive Imports
from app.api import tasks, errors
