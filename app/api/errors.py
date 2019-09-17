"""
Implement API error calls
"""

# # 3rd Party Modules
from flask import jsonify
from werkzeug import HTTP_STATUS_CODES


def error_response(status_code, message=None):
    """
    Implements error responses
    """
    payload = {'error': HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
    if message:
        payload['message'] = message
    respose = jsonify(payload)
    respose.status_code = status_code
    return respose


def bad_request(message):
    """
    Implement 400 error
    """
    return error_response(400, message)
