from flask import Flask, render_template
import uuid
from markupsafe import escape
from flask import jsonify

app = Flask(__name__)

empDB=[
 {
 'id':'101',
 'name':'Saravanan S',
 'title':'Technical Leader'
 },
 {
 'id':'201',
 'name':'Rajkumar P',
 'title':'Sr Software Engineer'
 }
]

@app.route('/empdb/employee',methods=['GET'])
def getAllEmp():
    return jsonify({'emps':empDB})

@app.route('/newid')
def idnew():
    newid = uuid.uuid4
    return jsonify({'id':newid})

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
def hello_world(name):
    return render_template('template.html', name=name)