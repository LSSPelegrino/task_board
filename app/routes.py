"""
Describes routes for web requests
"""

# # 3rd Party Modules
from flask import render_template
import requests

# # Internal Modules
from app import app


@app.route('/')
def home():
    """
    Renders the application homepage
    """
    page = 1
    per_page = 10
    response = requests.get(
        f"http://localhost:5000/api/tasks?page={page}&per_page={per_page}")
    tasks = response.json()["items"]

    return render_template('home.html', tasks=tasks)
