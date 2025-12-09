from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from src.utils.auth import login_required, role_required
from src.repositories.event_repo import (
    create_event,
    get_event_by_id,
    get_all_events,
    update_event,
    delete_event,
)

bp = Blueprint('events', __name__)


@bp.route('/events')
def events_list():
    events = get_all_events(status='approved')
    return render_template('events_list.html', events=events)


@bp.route('/event/<int:event_id>')
def event_detail(event_id):
    event = get_event_by_id(event_id)
    if not event:
        flash('Event not found', 'error')
        return redirect(url_for('events.events_list'))
    return render_template('event_datail.html', event=event)


@bp.route('/event/create', methods=['GET', 'POST'])
@login_required
def create_event_view():

    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        description = request.form.get('description', '').strip()
        location = request.form.get('location', '').strip()
        date = request.form.get('date', '').strip()
        time = request.form.get('time', '').strip()

        if not (title and description and location and date and time):
            flash('Please fill all event fields', 'error')
            return render_template('create_event.html')

        status = 'approved' if session.get('role') == 'organizer' else 'pending'
        eid = create_event(title, description, location, date, time, session['user_id'], status=status)
        if eid:
            msg = 'Event created successfully (approved)' if status == 'approved' else 'Event created successfully (pending approval)'
            flash(msg, 'success')
            return redirect(url_for('main.dashboard'))
        else:
            flash('Failed to create event', 'error')

    return render_template('create_event.html')


@bp.route('/event/<int:event_id>/edit', methods=['GET', 'POST'])
@login_required
@role_required('organizer')
def edit_event_view(event_id):

    event = get_event_by_id(event_id)
    if not event:
        flash('Event not found', 'error')
        return redirect(url_for('events.events_list'))

    if session.get('role') != 'organizer' or event.get('organizer_id') != session.get('user_id'):
        flash('You do not have permission to edit this event', 'error')
        return redirect(url_for('events.event_detail', event_id=event_id))

    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        description = request.form.get('description', '').strip()
        location = request.form.get('location', '').strip()
        date = request.form.get('date', '').strip()
        time = request.form.get('time', '').strip()
        status = request.form.get('status', event.get('status'))

        if not (title and description and location and date and time):
            flash('Please fill all event fields', 'error')
            return render_template('edit_event.html', event=event)

        ok = update_event(event_id, title, description, location, date, time, status)
        if ok:
            flash('Event updated', 'success')
            return redirect(url_for('events.event_detail', event_id=event_id))
        else:
            flash('Failed to update event', 'error')

    return render_template('edit_event.html', event=event)


@bp.route('/event/<int:event_id>/delete', methods=['POST'])
@login_required
@role_required('organizer')
def delete_event_view(event_id):

    event = get_event_by_id(event_id)
    if not event:
        flash('Event not found', 'error')
        return redirect(url_for('events.events_list'))

    if session.get('role') != 'organizer' or event.get('organizer_id') != session.get('user_id'):
        flash('You do not have permission to delete this event', 'error')
        return redirect(url_for('events.event_detail', event_id=event_id))

    if delete_event(event_id):
        flash('Event deleted', 'success')
    else:
        flash('Failed to delete event', 'error')
    return redirect(url_for('main.dashboard'))


@bp.route('/organizer/events')
@login_required
@role_required('organizer')
def organizer_events():
    organizer_id = session.get('user_id')
    from src.repositories.event_repo import get_events_by_organizer

    events = get_events_by_organizer(organizer_id)
    return render_template('organizer_events.html', events=events)
