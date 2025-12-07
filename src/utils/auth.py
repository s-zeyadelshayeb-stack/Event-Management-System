from functools import wraps
from flask import session, redirect, url_for, flash


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please login to continue', 'error')
            return redirect(url_for('auth.login'))
        return func(*args, **kwargs)

    return wrapper


def role_required(role):
    def deco(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if session.get('role') != role:
                flash('You do not have permission to access this page', 'error')
                return redirect(url_for('main.dashboard'))
            return func(*args, **kwargs)

        return wrapper

    return deco
