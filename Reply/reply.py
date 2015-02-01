from flask import Blueprint

reply = Blueprint('reply', __name__)


@reply.route('/reply')
def hello_world():
    return 'Reply'
