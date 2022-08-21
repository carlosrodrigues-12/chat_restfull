from crypt import methods
from flask import Flask, render_template
import uuid
from markupsafe import escape
from flask import jsonify

id = uuid.uuid4()
print(id)

app = Flask(__name__)

empDB=[
    {
        'chat_id':'1365468792',
        'from':'From user',
        'dest':'Bob',
        'msg':'Bom dia, tudo bem?'
    }
]

@app.route('/empdb/employee',methods=['GET'])
def getAllEmp():
    return jsonify({'emps':empDB})

@app.route('/newid',methods=['GET'])
def idnew():
    return id

@app.route('/sendMessage/<dest>/<msg>', methods=['GET','POST'])
def send_message(dest,msg):
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''
    # return f'New Message: Destinatario: {escape(dest)} Message: {escape(msg)}'

@app.route('/getMessage/<username>', methods=['GET'])
def getMessages(username):
    usr = [ emp for emp in empDB if (emp['dest'] == username)]
    return jsonify({'Messages':usr})

@app.route('/empdb/employee/<empId>',methods=['GET'])
def getEmp(empId):
    usr = [ emp for emp in empDB if (emp['id'] == empId) ] 
    return jsonify({'emp':usr})

@app.route("/")
def index():
    return "<p>Index Page<p>"

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_world(name):
    return render_template('template.html', name=name)