from flask import Flask
from modules import user

app = Flask(__name__)
app.register_blueprint(user)

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10101, debug=True)
