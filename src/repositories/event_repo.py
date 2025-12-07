from src.utils.db import get_db


def create_event(title, description, location, date, time, organizer_id, status='pending'):
    db = get_db()
    cur = db.cursor()
    try:
        cur.execute(
            """INSERT INTO events (title, description, location, date, time, status, organizer_id, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, datetime('now'))""",
            (title, description, location, date, time, status, organizer_id),
        )
        db.commit()
        return cur.lastrowid
    except Exception:
        db.rollback()
        return None


def get_event_by_id(event_id):
    db = get_db()
    cur = db.cursor()
    cur.execute(
        "SELECT id, title, description, location, date, time, status, organizer_id, created_at FROM events WHERE id = ?",
        (event_id,),
    )
    row = cur.fetchone()
    return dict(row) if row else None


def get_all_events(status=None):
    db = get_db()
    cur = db.cursor()
    if status:
        cur.execute(
            "SELECT id, title, description, location, date, time, status, organizer_id, created_at FROM events WHERE status = ? ORDER BY date ASC",
            (status,),
        )
    else:
        cur.execute(
            "SELECT id, title, description, location, date, time, status, organizer_id, created_at FROM events ORDER BY date ASC"
        )
    rows = cur.fetchall()
    return [dict(r) for r in rows]


def get_events_by_organizer(organizer_id):
    db = get_db()
    cur = db.cursor()
    cur.execute(
        "SELECT id, title, description, location, date, time, status, organizer_id, created_at FROM events WHERE organizer_id = ? ORDER BY date DESC",
        (organizer_id,),
    )
    rows = cur.fetchall()
    return [dict(r) for r in rows]


def update_event(event_id, title, description, location, date, time, status):
    db = get_db()
    cur = db.cursor()
    try:
        cur.execute(
            "UPDATE events SET title = ?, description = ?, location = ?, date = ?, time = ?, status = ? WHERE id = ?",
            (title, description, location, date, time, status, event_id),
        )
        db.commit()
        return True
    except Exception:
        db.rollback()
        return False


def delete_event(event_id):
    db = get_db()
    cur = db.cursor()
    try:
        cur.execute("DELETE FROM events WHERE id = ?", (event_id,))
        db.commit()
        return True
    except Exception:
        db.rollback()
        return False