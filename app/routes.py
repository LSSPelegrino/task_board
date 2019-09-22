"""
Describes routes for web requests
"""

# # Standard Modules
from datetime import datetime
import time


# # 3rd Party Modules
from flask import render_template, redirect, url_for, jsonify, flash
import requests
from dateutil import parser

# # Internal Modules
from app import app
from app.forms import CreateTaskForm
from app.forms import ToggleDoneForm


@app.route('/', methods=['GET', 'POST'])
def home():
    """
    Renders the application homepage
    """
    return render_template('home.html',
                           title="Home")


@app.route('/view_tasks', methods=['GET', 'POST'])
def view_tasks():
    """
    Renders the view task page
    """
    toggle_form = ToggleDoneForm()
    if toggle_form.validate_on_submit():
        requests.put(
            f"http://127.0.0.1:5000/api/tasks/{toggle_form.task_id.data}/toggle_done",
            headers={'Connection': 'close'})
        return redirect(url_for('view_tasks'))

    page = 1
    per_page = 100
    response = requests.get(
        f"http://127.0.0.1:5000/api/tasks?page={page}&per_page={per_page}",
        headers={'Connection': 'close'})
    tasks = response.json()["items"]
    for task in tasks:
        task['deadline'] = parser.parse(task['deadline'])
        task['completed_at'] = parser.parse(
            task['completed_at']) if task['done'] else None

    return render_template('view_tasks.html',
                           title='View Tasks',
                           tasks=tasks,
                           toggle_form=toggle_form)


@app.route('/post_task', methods=['GET', 'POST'])
def post_task():
    """
    Renders the create task page
    """
    create_form = CreateTaskForm()
    if create_form.validate_on_submit():
        data = {
            "title": create_form.title.data,
            "deadline": create_form.deadline.data.isoformat(
                timespec='milliseconds')
        }
        data.update({
            "description": create_form.description.data
            }) if create_form.description.data else None
        print(data)
        response = requests.post("http://127.0.0.1:5000/api/tasks",
                                 json=data)
        print(response.json())
        return redirect(url_for('view_tasks'))
    return render_template('create_task.html',
                           title='Post Task',
                           create_form=create_form)
