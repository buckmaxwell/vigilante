from flask import Blueprint

report = Blueprint('report', __name__, url_prefix='/report')


class Report:
    kind = 'report'         # class variable shared by all instances

    def __init__(self, title, severity, location, description):
        self.title = title
        self.severity = severity
        self.location = location
        self.description = description


@report.route('/')
def hello_world():
    return 'Report'


@report.route('/create', methods=['GET', 'POST'])
def create_report():
    _report = Report('Report1', 'severity', 'location', 'description')
    report_list = [_report.kind, _report.title, _report.description, _report.severity, _report.location]
    return str(report_list)


