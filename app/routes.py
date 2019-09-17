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
    tasks = [
        {
            'task_id': 1,
            'title': 'Do it',
            'description': 'Just do it',
            'deadline': '2015-04-15T10:41:00.000Z',
            'done': True,
            'completed_at': '2019-09-17T01:05:36.447Z'},
        {
            'task_id': 2,
            'title': 'Make your dreams come true',
            'description': "Don't let your dreams be dreams",
            'deadline': '2015-04-15T10:41:00.000Z',
            'done': False,
            'completed_at': None},
        {
            'task_id': 3,
            'title': 'Rock the casbah',
            'description': 'You have to let that raga drop',
            'deadline': '1982-01-01T00:00:00.000Z',
            'done': True,
            'completed_at': '2019-09-15T04:16:42.595Z'},
        {
            'task_id': 4,
            'title': 'Be yourself',
            'description': 'All that I can do',
            'deadline': '2005-02-02T00:00:00.000Z',
            'done': False,
            'completed_at': None},
        {
            'task_id': 5,
            'title': 'first API call',
            'description': 'First Time using PUT',
            'deadline': '2019-09-16T17:12:00.000Z',
            'done': False,
            'completed_at': None},
        {
            'task_id': 6,
            'title': 'Get up, stand up',
            'description': "Don't give up the fight",
            'deadline': '1981-05-11T05:00:00.000Z',
            'done': False,
            'completed_at': None}
    ]
    return render_template('home.html', tasks=tasks)
