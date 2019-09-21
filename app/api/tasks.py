"""
Implement API calls with tasks
"""

# # Standard Modules
import re
import time

# # 3rd Party Modules
from flask import request, jsonify
from flask_restful import Resource

# # Internal Modules
from app import db
from app.api import api
from app.models import Task, DoneTask
from app.api.errors import bad_request, error_response


def date_validate(date: str):
    """
    Validate if string is in ISO-86001 format
    """
    # Regular expressions are not pretty
    if re.search(('^(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0'
                  '-2]|0[1-9])-(3[01]|0[1-9]|[12][0-9])T'
                  '(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5'
                  '][0-9])(\\.[0-9]{3})?(Z|[+-](?:2[0-3]|[0'
                  '1][0-9]):[0-5][0-9])?$'
                  ), date) is None:
        return False, 'deadline format must be YYYY-MM-DDThh:mm:ss.uuu±ZZ:ZZ'
    return True, ''


class ApiTaskId(Resource):
    """
    Defines resource class for task's id
    """
    def get(self, task_id):
        """
        Implement GET method
        """
        return jsonify(Task.query.get_or_404(task_id).to_dict())

    def put(self, task_id):
        """
        Implement PUT method
        """
        task = Task.query.get_or_404(task_id)
        data = request.get_json() or {}
        if 'deadline' in data:
            is_valid, message = date_validate(data['deadline'])
            if not is_valid:
                return bad_request(message)
        task.from_dict(data)
        db.session.commit()
        return jsonify(task.to_dict())


class ApiTask(Resource):
    """
    Defines resource class for task
    """
    def post(self):
        """
        Implement POST method
        """
        data = request.get_json() or {}
        if 'title' not in data or \
                'deadline' not in data:
            return bad_request('must include at least title and deadline')
        is_valid, message = date_validate(data['deadline'])
        if not is_valid:
            return bad_request(message)
        task = Task()
        task.from_dict(data)
        db.session.add(task)
        db.session.commit()
        response = jsonify(task.to_dict())
        response.status_code = 201
        response.headers['Location'] = api.url_for(ApiTaskId,
                                                   task_id=task.task_id)
        return response

    def get(self):
        """
        Implement GET method
        """
        page = request.args.get('page', 1, type=int)
        per_page = min(request.args.get('per_page', 10, type=int), 100)
        data = Task.to_collection_dict(Task.query, page, per_page)
        end = time.time()
        return data


class ApiTaskToggleDone(Resource):
    """
    Defines resource class for task done
    """

    def put(self, task_id):
        """
        Implement PUT method
        """
        task = Task.query.get(task_id)
        if not task:
            return error_response(404, "There is no task with this id")
        if task.done:
            done_task = DoneTask.query.filter_by(task_id=task_id).first()
            db.session.delete(done_task)
        else:
            done_task = DoneTask(task_done=task)
            db.session.add(done_task)
        db.session.commit()
        return jsonify(task.to_dict())


api.add_resource(ApiTask, '/api/tasks')
api.add_resource(ApiTaskId, '/api/tasks/<int:task_id>')
api.add_resource(ApiTaskToggleDone, '/api/tasks/<int:task_id>/toggle_done')
