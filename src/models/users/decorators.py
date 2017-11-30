from functools import wraps
from src import config

from flask import redirect, url_for, session, request

def requires_login(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if 'email' not in session.keys() or session['email'] == None:
            return redirect(url_for('users.login_user', next=request.path))
        return func(*args, **kwargs)
    return decorated_function


def requires_admin_permissions(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if 'email' not in session.keys() or session['email'] == None:
            return redirect(url_for('users.login_user', next=request.path))
        if session['email'] not in config.ADMINS:
            return redirect(url_for('users.login_user'))
        return func(*args, **kwargs)
    return decorated_function

