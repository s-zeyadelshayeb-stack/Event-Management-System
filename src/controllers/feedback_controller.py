from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from src.repositories.feedback_repo import submit_feedback, get_event_feedbacks
from src.repositories.registration_repo import is_user_registered
from src.repositories.event_repo import get_event_by_id

bp = Blueprint('feedback', __name__)


@bp.route('/feedback/<int:event_id>', methods=['GET', 'POST'])
def feedback(event_id):
    if 'user_id' not in session:
        flash('Please login to leave feedback', 'error')
        return redirect(url_for('auth.login'))

    event = get_event_by_id(event_id)
    if not event:
        flash('Event not found', 'error')
        return redirect(url_for('events.events_list'))

    is_organizer = session.get('role') == 'organizer' and session.get('user_id') == event.get('organizer_id')
    if not is_organizer and not is_user_registered(session['user_id'], event_id):
        flash('You must be registered to leave feedback', 'error')
        return redirect(url_for('events.event_detail', event_id=event_id))

    if request.method == 'POST':
        # Only students may submit feedback
        if session.get('role') != 'student':
            flash('Only students can submit feedback', 'error')
            return redirect(url_for('events.event_detail', event_id=event_id))

        try:
            rating = int(request.form.get('rating', 0))
        except ValueError:
            rating = 0
        comment = request.form.get('comment', '').strip()

        if rating < 1 or rating > 5:
            flash('Please provide a valid rating (1-5)', 'error')
            return redirect(url_for('feedback.feedback', event_id=event_id))

        fid = submit_feedback(session['user_id'], event_id, rating, comment)
        if fid:
            flash('Feedback submitted, thank you!', 'success')
            return redirect(url_for('events.event_detail', event_id=event_id))
        else:
            flash('Failed to submit feedback', 'error')

    feedbacks = get_event_feedbacks(event_id)
    return render_template('feedback.html', feedbacks=feedbacks, event=event)
