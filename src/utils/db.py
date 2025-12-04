import sqlite3
from flask import g
import os

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), '..', 'app.db')

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DB_PATH)
        db.row_factory = sqlite3.Row
    return db

def close_db(app):
    @app.teardown_appcontext
    def _close_db(exception):
        db = getattr(g, '_database', None)
        if db is not None:
            db.close()
