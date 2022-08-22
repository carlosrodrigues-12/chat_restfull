from flask import Flask, render_template, request, session, redirect, url_for
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.getenv('SECRET','randomstring123')

messages = []

def add_message(remt,dest,msg):
    moment = datetime.now().strftime("%H:%M:%S")
    messages.append({"timestamp": moment, "remt": remt, "dest": dest, "message": msg})

@app.route('/', methods=['POST'])
def login_user():


@app.route('/sendMessage/<dest>/<msg>', methods=['GET','POST'])
def send_message(dest,msg):
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route("/", methods=['GET','POST'])
def index():
    if request.method == "POST":
        session["username"] = request.form["username"]

    if "username" in session:
        return redirect(url_for("user", username=session["username"]))

    return render_template("index.html")

@app.route("/chat/<username>", methods=['GET','POST'])
def user(username):
    if request.method == 'POST':
        username = session["username"]
        message = request.form["message"]
        add_message(username,'teste', message)
        return redirect(url_for("user", username=session["username"]))

    return render_template('template.html', username=username, chat_messages=messages)

app.run(host=os.getenv('IP','0.0.0.0'),port=int(os.getenv('PORT','5000')),debug=True)