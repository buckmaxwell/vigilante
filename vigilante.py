from flask import Flask
from User import user
from Report import report

app = Flask(__name__)
app.register_blueprint(user.user)
app.register_blueprint(report.report)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10101, debug=True)
