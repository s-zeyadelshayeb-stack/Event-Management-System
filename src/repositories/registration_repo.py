from src.utils.db import get_db


def register_user(student_id, event_id):
    db = get_db()
    cur = db.cursor()
    try:
        cur.execute(
            "INSERT INTO registrations (student_id, event_id, status, registration_date) VALUES (?, ?, 'registered', datetime('now'))",
            (student_id, event_id),
        )
        db.commit()
        return cur.lastrowid
    except Exception:
        db.rollback()
        return None


def is_user_registered(student_id, event_id):
    db = get_db()
    cur = db.cursor()
    cur.execute(
        "SELECT id FROM registrations WHERE student_id = ? AND event_id = ? AND status = 'registered'",
        (student_id, event_id),
    )
    return cur.fetchone() is not None


def get_user_registrations(student_id):
    db = get_db()
    cur = db.cursor()
    cur.execute(
        "SELECT r.id, r.student_id, r.event_id, r.status, r.registration_date, e.title, e.date FROM registrations r JOIN events e ON r.event_id = e.id WHERE r.student_id = ? ORDER BY r.registration_date DESC",
        (student_id,),
    )
    rows = cur.fetchall()
    return [dict(r) for r in rows]


def get_registration(registration_id):
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT id, student_id, event_id, status, registration_date FROM registrations WHERE id = ?", (registration_id,))
    row = cur.fetchone()
    return dict(row) if row else None


def cancel_registration(registration_id):
    db = get_db()
    cur = db.cursor()
    try:
        cur.execute("UPDATE registrations SET status = 'cancelled' WHERE id = ?", (registration_id,))
        db.commit()
        return True
    except Exception:
        db.rollback()
        return False


def mark_attended(registration_id):
    db = get_db()
    cur = db.cursor()
    try:
        cur.execute("UPDATE registrations SET status = 'attended' WHERE id = ?", (registration_id,))
        db.commit()
        return True
    except Exception:
        db.rollback()
        return False
    