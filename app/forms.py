"""
Implement Form classes
"""

# # 3rd Patry Modules
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import TextAreaField
# from wtforms import DateTimeField
from wtforms import HiddenField
from wtforms import SubmitField
from wtforms.validators import DataRequired
from wtforms.validators import Length
from wtforms.fields.html5 import DateTimeLocalField


class CreateTaskForm(FlaskForm):
    """
    Form class for creating a Task
    """
    title = StringField('Title',
                        validators=[DataRequired()])
    description = TextAreaField('Description',
                                validators=[Length(min=0, max=200)])
    deadline = StringField('Deadline', validators=[DataRequired()])
    submit = SubmitField('Create Task')


class ToggleDoneForm(FlaskForm):
    """
    Form class to mark task as Done and back
    """
    task_id = HiddenField('Task ID')
    button = SubmitField('Toggle Done')
