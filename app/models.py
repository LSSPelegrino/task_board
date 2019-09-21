"""
Implement database models
"""

# # Standard Modules
from datetime import datetime, timezone

# # 3rd Party Modules
from dateutil import parser

# # Internal Modules
from app import db
# from app.api import api


class PaginatedAPIMixin(object):
    """
    Mixin class to generate a dictionary with paginated information of queries
    """
    @staticmethod
    def to_collection_dict(query: db.Model,
                           page: int,
                           per_page: int,
                           **kwargs):
        """
        Generate a dicionary with paginated information of queries
        """
        resources = query.paginate(page, per_page, False)
        data = {
            'items': [item.to_dict() for item in resources.items],
            '_meta': {
                'page': page,
                'per_page': per_page,
                'total_pages': resources.pages,
                'total_items': resources.total
            }
        }
        return data


class Task(PaginatedAPIMixin, db.Model):
    """
    Model for the tasks table
    """
    __tablename__ = 'task'
    task_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    description = db.Column(db.String(200))
    deadline = db.Column(db.DateTime)
    done = db.relationship('DoneTask', backref='task_done', uselist=False)

    def __repr__(self):  # REDO
        return (
            f'task_id: {self.task_id} \n'
            f'title: {self.title} \n'
            f'description: {self.description} \n'
            f'deadline: {self.deadline} \n'
            f'related done task table: \n'
            f'{self.done} \n'
        )

    def to_dict(self):
        """
        Returns a dictionary
        """
        data = {
            'task_id': self.task_id,
            'title': self.title,
            'description': self.description,
            'deadline': self.deadline.isoformat(
                timespec='milliseconds') + 'Z',
            'done': True if self.done else False,
            'completed_at': self.done.completed_at.isoformat(
                timespec='milliseconds') + 'Z' if self.done else None
        }
        return data

    def from_dict(self, data: dict):
        """
        Fill parameters with data from dictionary
        """
        if 'title' in data:
            self.title = data['title']
        if 'description' in data:
            self.description = data['description']
        if 'deadline' in data:
            self.deadline = parser.parse(data['deadline'])
        return


class DoneTask(db.Model):
    """
    Model for the done tasks table
    """
    __tablename__ = 'done_task'
    done_task_id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('task.task_id'), unique=True)
    completed_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):  # REDO
        return (
            f'done_task_id: {self.done_task_id} \n'
            f'task_id: {self.task_id} \n'
            f'completed_at: {self.completed_at} \n'
        )
