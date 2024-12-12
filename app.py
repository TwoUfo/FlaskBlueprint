from flask import Flask
from first import first_bp
from second import second_bp


def create_app():
    app = Flask(__name__)
    first_bp.register_blueprint(second_bp)
    app.register_blueprint(first_bp)
    
    return app
