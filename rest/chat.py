import uuid
import os
from flask import Flask, request, session, jsonify
from datetime import datetime

app = Flask(__name__)

messages = []

def add_message(remt,dest,msg):
    id_msg = 0
    moment = datetime.now().strftime("%H:%M:%S")
    messages.append({"timestamp": moment, "remt": remt, "dest": dest, "message": msg, "id_msg": id_msg+1})

@app.route('/sendMessage/<remt>/<dest>/<msg>', methods=['POST'])
def send_message(remt,dest,msg):
    add_message(remt,dest,msg)
    
    return jsonify(messages)

@app.route("/getMessages/<username>", methods=['GET','POST'])
def getMessages(username):
    msgs = [ msg for msg in messages if (msg['dest'] == username) ]
    return jsonify({'msg':msgs})

app.run(host=os.getenv('IP','0.0.0.0'),port=int(os.getenv('PORT','5000')),debug=True)