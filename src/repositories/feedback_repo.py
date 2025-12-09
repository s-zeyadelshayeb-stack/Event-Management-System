from src.utils.db import get_db


def submit_feedback(student_id, event_id, rating, comment=None):
    db = get_db()
    cur = db.cursor()
    try:
        cur.execute(
            "INSERT INTO feedbacks (student_id, event_id, rating, comment, created_at) VALUES (?, ?, ?, ?, datetime('now'))",
            (student_id, event_id, rating, comment),
        )
        db.commit()
        return cur.lastrowid
    except Exception:
        db.rollback()
        return None


def get_event_feedbacks(event_id):
    db = get_db()
    cur = db.cursor()
    cur.execute(
        "SELECT f.id, f.student_id, f.event_id, f.rating, f.comment, f.created_at, u.name FROM feedbacks f JOIN users u ON f.student_id = u.id WHERE f.event_id = ? ORDER BY f.created_at DESC",
        (event_id,),
    )
    rows = cur.fetchall()
    return [dict(r) for r in rows]


def get_user_feedback(student_id, event_id):
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT id, student_id, event_id, rating, comment, created_at FROM feedbacks WHERE student_id = ? AND event_id = ?", (student_id, event_id))
    row = cur.fetchone()
    return dict(row) if row else None


def get_feedback(feedback_id):
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT id, student_id, event_id, rating, comment, created_at FROM feedbacks WHERE id = ?", (feedback_id,))
    row = cur.fetchone()
    return dict(row) if row else None

