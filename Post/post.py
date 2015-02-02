from flask import Blueprint
import psycopg2
from uuid import uuid4
from datetime import datetime

report = Blueprint('report', __name__, url_prefix='/post')


class Post(object):
    @staticmethod
    def get_connection():
        return psycopg2.connect("dbname='vigilante' user='max'")

    @staticmethod
    def get_user_id(self, token):
        conn = Post.get_connection()
        db_conn = conn.cursor()
        db_conn.execute("SELECT userid from vigilante_dev_v1.session_token where token=%s", [token])
        for row in db_conn.fetchall():
            return row[0]
        return "bad token"

    @staticmethod
    def get_time():
            return datetime.datetime.now().isoformat()

    @staticmethod
    def get_id():
        return uuid4()
