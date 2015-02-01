from flask import Blueprint

user = Blueprint('user', __name__)


@user.route('/user')
def hello_world():
    return 'User'
