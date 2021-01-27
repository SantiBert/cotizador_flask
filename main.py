from flask import Flask, render_template
from flask_sockets import Sockets

app = Flask(__name__)
sockets = Sockets(app)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    socketio.run(app)
