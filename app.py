from flask import Flask, redirect, url_for
from src.utils.db import close_db 

def create_app():
    app = Flask(__name__)
    app.secret_key = 'dev-secret-change-this'

    from src.controllers.event_controller import bp as events_bp
    from src.controllers.registration_controller import bp as registration_bp
    from src.controllers.feedback_controller import bp as feedback_bp
    from src.controllers.auth_controller import bp as auth_bp
    from src.controllers.main import bp as main_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(events_bp)
    app.register_blueprint(registration_bp)
    app.register_blueprint(feedback_bp)

    @app.route('/')
    def home():
        return redirect(url_for('auth.login'))
    close_db(app)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
