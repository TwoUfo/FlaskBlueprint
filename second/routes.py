from flask import render_template, abort
from jinja2 import TemplateNotFound
from . import second_bp

@second_bp.route('/hello')
def show_test():
    try:
        return render_template('hello.html')
    except TemplateNotFound:
        abort(404)
