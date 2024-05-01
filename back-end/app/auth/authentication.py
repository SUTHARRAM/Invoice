# authentication.py
from functools import wraps
from flask import request, jsonify

def authenticate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth = request.authorization
        if auth and auth.username == 'username' and auth.password == 'password':
            return func(*args, **kwargs)
        return jsonify({'message': 'Unauthorized'}), 401
    return wrapper
