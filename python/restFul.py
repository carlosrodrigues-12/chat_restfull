from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/sendMessage/<dest>/<msg>')
def send_message(dest,msg):
    return f'New Message: Destinatario: {escape(dest)} Message: {escape(msg)}'

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {escape(username)}'

@app.route("/")
def index():
    return "<p>Index Page<p>"

@app.route("/hello")
def hello_world():
        return "<p>Hello, World!<p>"