from flask import Blueprint

profile = Blueprint('users', __name__, url_prefix='/users')

@profile.route('/')
def hello_world():
    return 'Hello World 2!'
