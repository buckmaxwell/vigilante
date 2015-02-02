from flask import Blueprint, jsonify, request
from Post import post
from urllib2 import Request, urlopen, URLError
import json

report = Blueprint('report', __name__, url_prefix='/report')


class Report(post.Post):
    def __init__(self, title, location, token, severity=0, description=''):
        self.token = token
        self.user_id = post.Post.get_user_id()
        self.title = title
        self.location = location
        self.severity = severity
        self.description = description
        self.lon = Report.get_location(location)[0]
        self.lat = Report.get_location(location)[1]

    def get_location(self):
        api_key = "AIzaSyAgw7ZFrTPcUB3okQqv8Ii2fNu_7091a_M"
        location = self.location.replace(" ", "+")
        lonlat = []
        req_str = "https://maps.googleapis.com/maps/api/geocode/json?address="+location+"key="+api_key
        try:
            _request = Request(req_str)
            response = urlopen(_request)
            location_json = json.loads(response.read())
            if len(location_json["results"]):
                lon = location_json["results"][0]["geometry"]["location"]["lng"]
                lat = location_json["results"][0]["geometry"]["location"]["lat"]
                lonlat.append(lon)
                lonlat.append(lat)
            else:
                print "woa there--that doesn't look like a real location"
        except URLError, e:
            print "Got an error code :(" + str(e)
        return lonlat


@report.route('/')
def hello_world():
    return 'Report'


@report.route('/create', methods=['GET', 'POST'])
def create_report():
    token = request.args.get('token')
    if 'title' not in request.json or 'location' not in request.json:
        return jsonify({'ERROR': 'no title in request.json'})
    if post.Post.validate_token(token):
        title = request.json['title']
        location = request.json['location']
        severity = request.json.get('severity', 0)
        description = request.json.get('description', 0)
        _report = Report(title, location, token, severity, description)
        db_conn = _report.conn.cursor()
        db_conn.execute("INSERT INTO vigilante_dev_v1.report(id, userid, title, time, longitude, latitude, severity, location, description) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)", (_report.id, _report.user_id, _report.title, _report.time, _report.lon, _report.lat, _report.severity, _report.location, _report.description))
        _report.conn.commit()
        return jsonify({'result': True})
    else:
        return jsonify({'result': True})