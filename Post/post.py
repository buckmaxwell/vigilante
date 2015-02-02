from flask import Blueprint
import psycopg2
from uuid import uuid4
from datetime import datetime

report = Blueprint('report', __name__, url_prefix='/post')


class Post:
    kind = 'Post'
    time = datetime.datetime.now().isoformat()
    id = uuid4()
    conn = psycopg2.connect("dbname='vigilante' user='max'")

    def __init__(self):
        self.token = None
        self.user_id = None
        self.title = None
        self.location = None
        self.severity = 0
        self.description = None
        self.lon = None
        self.lat = None
        print "base class--should never be called!"

    def get_user_id(self):
        conn = self.conn
        db_conn = conn.cursor()
        db_conn.execute("SELECT userid from vigilante_dev_v1.session_token where token=%s", [self.token])
        for row in db_conn.fetchall():
            return row[0]
        return "bad token"

    def check_token(self):
        conn = self.conn
        db_conn = conn.cursor()
        db_conn.execute("SELECT * from vigilante_dev_v1.session_token where token=%s", [str(self.token)])
        return db_conn.fetchall()

    def validate_token(self):
        if not self.token:
            return False
        if not Post.check_token():
            return False
        else:
            return True