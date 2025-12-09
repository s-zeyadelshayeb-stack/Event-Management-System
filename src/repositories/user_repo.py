from src.utils.db import get_db

def create_user(name, email, password_hash, role='student'):
    db = get_db()
    cur = db.cursor()
    try:
        cur.execute(
            "INSERT INTO users (name, email, password_hash, role) VALUES (?, ?, ?, ?)",
            (name, email, password_hash, role)
        )
        db.commit()
        return cur.lastrowid
    except Exception as e:
        db.rollback()
        return None

def get_user_by_email(email):
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT id, name, email, password_hash, role FROM users WHERE email = ?", (email,))
    row = cur.fetchone()
    return dict(row) if row else None

def get_user_by_id(user_id):
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT id, name, email, role FROM users WHERE id = ?", (user_id,))
    row = cur.fetchone()
    return dict(row) if row else None
def update_user_role(user_id, new_role):
    db = get_db()
    cur = db.cursor()
    try:
        cur.execute(
            "UPDATE users SET role = ? WHERE id = ?",
            (new_role, user_id)
        )
        db.commit()
        return cur.rowcount > 0
    except Exception as e:
        db.rollback()
        return False
def delete_user(user_id):
    db = get_db()
    cur = db.cursor()
    try:
        cur.execute("DELETE FROM users WHERE id = ?", (user_id,))
        db.commit()
        return cur.rowcount > 0
    except Exception as e:
        db.rollback()
        return False
def get_all_users():
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT id, name, email, role FROM users")
    rows = cur.fetchall()
    return [dict(row) for row in rows]
def update_user_password(user_id, new_password_hash):
    db = get_db()
    cur = db.cursor()
    try:
        cur.execute(
            "UPDATE users SET password_hash = ? WHERE id = ?",
            (new_password_hash, user_id)
        )
        db.commit()
        return cur.rowcount > 0
    except Exception as e:
        db.rollback()
        return False

