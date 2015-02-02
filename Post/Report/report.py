from flask import Blueprint
import Post

report = Blueprint('report', __name__, url_prefix='/report')


class Report(Post):
    kind = 'report'         # class variable shared by all instances

    def __init__(self, title, location, token, severity=0, description=''):
        self.id = Report.get_id()
        self.user_id = get_user_id(token)
        self.title = title
        self.time = Post.get_time()
        self.lon = Report.get_lon()
        self.lat = Report.get_lat()
        self.severity = severity
        self.location = location
        self.description = description


@report.route('/')
def hello_world():
    return 'Report'


def get_user_id(token):
    return Post.get_user_id(token)


@report.route('/create', methods=['GET', 'POST'])
def create_report():
    _report = Report('Report1', 'severity', 'location', 'description')
    report_list = [_report.kind, _report.title, _report.description, _report.severity, _report.location]
    return str(report_list)