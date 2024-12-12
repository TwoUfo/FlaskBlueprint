from flask import Blueprint

second_bp = Blueprint('second_bp', __name__, template_folder='templates')

from . import routes
