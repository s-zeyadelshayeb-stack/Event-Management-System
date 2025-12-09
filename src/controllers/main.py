from flask import Blueprint, render_template, redirect, url_for, g, session
from src.repositories.event_repo import get_all_events, get_events_by_organizer
from src.repositories.registration_repo import get_user_registrations

bp = Blueprint('main', __name__)


@bp.route('/dashboard')
def dashboard():
	if not getattr(g, 'user', None):
		return redirect(url_for('auth.login'))

	user = g.user

	events = get_all_events(status='approved') or []

	my_events = []
	if user and user.get('role') == 'organizer':
		my_events = get_events_by_organizer(user.get('id')) or []

	my_registrations = []
	if user:
		try:
			my_registrations = get_user_registrations(user.get('id')) or []
		except Exception:
			my_registrations = []

	return render_template(
		'dashboard.html', user=user, events=events, my_events=my_events, registrations=my_registrations
	)


