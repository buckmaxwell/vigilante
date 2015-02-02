from flask import Blueprint

reply = Blueprint('reply', __name__, url_prefix='/reply')


@reply.route('/')
def hello_world():
    return 'Reply'
