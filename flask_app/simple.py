"""A simple example explaining GET, POST.

  Reference: http://flask_app.pocoo.org/docs/1.0/quickstart/#a-minimal-application
"""

from flask import Blueprint, render_template, request
bp = Blueprint('simple', __name__)


@bp.route('/simple', methods=['GET', 'POST'])
def simple_handler():
    if request.method == 'GET':
        return render_template('simple.html')
