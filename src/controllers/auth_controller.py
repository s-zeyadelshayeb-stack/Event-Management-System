from flask import Blueprint, render_template, request, redirect, url_for, flash, session, g
from src.repositories.user_repo import create_user, get_user_by_email, get_user_by_id
from src.utils.security import hash_password, verify_password

bp = Blueprint('auth', __name__)

@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')
        password2 = request.form.get('password2', '')

        if not name or not email or not password:
            flash('Please fill required fields', 'error')
            return render_template('signup.html')

        if password != password2:
            flash('Passwords do not match', 'error')
            return render_template('signup.html')

        if get_user_by_email(email):
            flash('Email already registered', 'error')
            return render_template('signup.html')

        pw_hash = hash_password(password)
        role = request.form.get('role', 'student')
        if role not in ('student', 'organizer'):
            role = 'student'
        user_id = create_user(name, email, pw_hash, role=role)
        if user_id:
            flash('Account created. Please login.', 'success')
            return redirect(url_for('auth.login'))
        else:
            flash('Failed to create account', 'error')

    return render_template('signup.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')

        user = get_user_by_email(email)
        if user and verify_password(user['password_hash'], password):
            session.clear()
            session['user_id'] = user['id']
            session['user_name'] = user['name']
            session['role'] = user['role']
            flash('Logged in successfully', 'success')
            return redirect(url_for('main.dashboard'))  
        else:
            flash('Invalid email or password', 'error')
            return render_template('login.html')

    return render_template('login.html')

@bp.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out', 'info')
    return redirect(url_for('auth.login'))

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = get_user_by_id(user_id)

