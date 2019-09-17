"""
Describes routes for web requests
"""

# # 3rd Party Modules
from flask import render_template

# # Internal Modules
from app import app


@app.route('/')
def home():
    """
    Renders the application homepage
    """
    return render_template('home.html')
