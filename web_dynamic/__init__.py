from flask import Flask, render_template
from .auth import auth_bp
from .admin import admin_bp
from .main import main_bp
from models import storage
from dotenv import load_dotenv
from os import getenv
from datetime import timedelta

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.secret_key = 'aef235ef0847657f62f918f89056d2416a602afa5bf21adb058bfab47b0613f7'

    # Secure session cookie settings
    app.config['SESSION_COOKIE_SECURE'] = True
    app.config['SESSION_COOKIE_HTTPONLY'] = True
    app.config['SESSION_COOKIE_SAMESITE'] = 'Strict'
    app.config['SESSION_COOKIE_NAME'] = '__Host-session'
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)


    @app.after_request
    def apply_security_headers(response):
        csp = (
        "default-src 'self'; "
        "script-src 'self' https://ajax.googleapis.com; "
        "style-src 'self' https://fonts.googleapis.com; "
        "font-src 'self' https://fonts.gstatic.com;"
        )
        response.headers['Content-Security-Policy'] = csp
        response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['X-Frame-Options'] = 'DENY'
        return response

    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(main_bp)

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('page_not_found.html'), 404

    @app.teardown_appcontext
    def close_db(error):
        """ Remove the current SQLAlchemy Session """
        storage.close()
    
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('page_not_found.html'), 4
    
    @app.route('/favicon.ico')
    def favicon():
        return '', 204

    return app
