from flask import Blueprint, redirect, url_for, flash, session
from src.repositories.registration_repo import register_user, is_user_registered, cancel_registration, get_registration

bp = Blueprint('registration', _name_)


def _is_student():
    return session.get('role') == 'student'


@bp.route('/register/<int:event_id>', methods=['POST'])
def register(event_id):
    if 'user_id' not in session:
        flash('Please login to register', 'error')
        return redirect(url_for('auth.login'))

    if not _is_student():
        flash('Only students can register for events', 'error')
        return redirect(url_for('events.event_detail', event_id=event_id))

    user_id = session['user_id']
    if is_user_registered(user_id, event_id):
        flash('You are already registered for this event', 'info')
        return redirect(url_for('events.event_detail', event_id=event_id))

    reg_id = register_user(user_id, event_id)
    if reg_id:
        flash('Registration successful', 'success')
    else:
        flash('Registration failed', 'error')
    return redirect(url_for('events.event_detail', event_id=event_id))


@bp.route('/unregister/<int:registration_id>', methods=['POST'])
def unregister(registration_id):
    if 'user_id' not in session:
        flash('Please login', 'error')
        return redirect(url_for('auth.login'))

    if not _is_student():
        flash('Only students can cancel registrations', 'error')
        return redirect(url_for('main.dashboard'))

    reg = get_registration(registration_id)
    if not reg:
        flash('Registration not found', 'error')
        return redirect(url_for('main.dashboard'))

    if reg.get('student_id') != session.get('user_id'):
        flash('You do not have permission to cancel this registration', 'error')
        return redirect(url_for('main.dashboard'))

    if cancel_registration(registration_id):
        flash('Registration cancelled', 'success')
    else:
        flash('Failed to cancel registration', 'error')
    return redirect(url_for('main.dashboard'))