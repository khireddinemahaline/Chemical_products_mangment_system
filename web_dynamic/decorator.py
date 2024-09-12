from functools import wraps
from flask import session, redirect, url_for, flash
from models import storage, User

def role_required(role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            user_id = session.get('user_id')
            user = storage.get(User, user_id)
            if user and user.role == role:
                return f(*args, **kwargs)
            else:
                flash(f'Access denied for {role} only.', 'error')
                return redirect(url_for('auth.signin'))
        return decorated_function
    return decorator
