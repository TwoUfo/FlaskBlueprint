from flask import render_template, abort
from jinja2 import TemplateNotFound
from . import first_bp

@first_bp.route('/test')
def show_test():
    try:
        return render_template('test.html')
    except TemplateNotFound:
        abort(404)
