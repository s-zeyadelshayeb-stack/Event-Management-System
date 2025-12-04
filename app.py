from flask import Flask, redirect, url_for
from src.utils.db import close_db

def create_app():
    app = Flask(__name__)
    app.secret_key = 'dev-secret-change-this'

    from src.controllers.auth_controller import bp as auth_bp
    app.register_blueprint(auth_bp)

    @app.route('/')
    def home():
        return redirect(url_for('auth.login'))

    @app.route('/dashboard')
    def temp_dashboard():
        return "<h1>Dashboard will appear here once team adds it.</h1>"

    close_db(app)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
