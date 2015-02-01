from flask import Blueprint

report = Blueprint('report', __name__)


@report.route('/report')
def hello_world():
    return 'Report'