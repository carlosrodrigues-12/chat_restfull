from flask import Flask, render_template
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

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_world(name=None):
    return render_template('template.html', name=name)