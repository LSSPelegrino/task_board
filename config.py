"""
Describes configuration of Flask
"""

# # Standard Modules
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """
    Set Flask's configuration variables
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'this-is-a-password'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
