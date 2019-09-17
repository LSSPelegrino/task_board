"""
Main Flask Application
"""

# # Internal Modules
from app import app
from app import api
from app import db
from app.models import Task, DoneTask


@app.shell_context_processor
def make_shell_context():
    """
    Add keywords to the shell context.
    Run $ flask shell' to have' access on the command line
    """
    return {'db': db, 'Task': Task, 'DoneTask': DoneTask}
