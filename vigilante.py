from flask import Flask
from Post.Reply import reply
from Post.Report import report
from Post.User import user
from Post import post


app = Flask(__name__)
app.register_blueprint(user.user)
app.register_blueprint(report.report)
app.register_blueprint(reply.reply)
app.register_blueprint(post.post)


@app.route('/')
@app.route('/index')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10101, debug=True)
