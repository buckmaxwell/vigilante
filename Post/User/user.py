from flask import Blueprint, jsonify, request
from Post import post
from Crypto.Hash import SHA256

user = Blueprint('user', __name__, url_prefix='/user')


class User(post.Post):
    def __init__(self, username, password):
        self.username = username
        self.strikes = 0
        self.password_hash = User.generate_hash(password)
        self.active = True

    @staticmethod
    def generate_hash(password):
        new_hash = SHA256.new()
        new_hash.update(password)
        return new_hash


@user.route('/')
def hello_world():
    return 'User'


@user.route('/create', methods=['GET', 'POST'])
def create_user():
    if 'username' not in request.json or 'password' not in request.json:
        return jsonify({'ERROR': 'no username or password'})
    username = request.json['username']
    password = request.json['password']
    _user = User(username, password)
    conn = _user.conn
    db_conn = conn.cursor()
    db_conn.execute("SELECT * from vigilante_dev_v1.user where username=%s", (username, ))
    if not db_conn.fetchall():
        db_conn.execute("INSERT INTO vigilante_dev_v1.user(id, username, strikes, passwordhash, active) VALUES (%s,%s,%s,%s,%s)", (_user.id, _user.username, _user.strikes, buffer(_user.password_hash.digest()), _user.active))
        conn.commit()
        return jsonify({'Result': True})
    return jsonify({'ERROR': 'username already exists!'})





