from flask import Flask, render_template
from .auth import auth_bp
from .admin import admin_bp
from .main import main_bp
from models import storage
from dotenv import load_dotenv
from os import getenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.secret_key = 'aef235ef0847657f62f918f89056d2416a602afa5bf21adb058bfab47b0613f7'

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
