from flask import Blueprint

first_bp = Blueprint('first_bp', __name__, template_folder='templates', url_prefix='/first')

from . import routes