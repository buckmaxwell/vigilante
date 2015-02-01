from flask import Blueprint

report = Blueprint('report', __name__, url_prefix='/report')


@report.route('/')
def hello_world():
    return 'Report'