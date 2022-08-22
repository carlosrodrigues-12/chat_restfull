
from flask import Flask
from flask import jsonify
from flask import request
import sys
import const 
import requests
import threading

app = Flask(__name__)

@app.route('/chat',methods=['POST'])
def createEmp():

    dados = {
    'dest':request.json['dest'],
    'name':request.json['name'],
    'msg':request.json['msg'],
    'id':request.json['id'],
    }

    if(request.json['id'] == ''):
        print(str(request.json['count']) + " - MSG: " + request.json['msg'] + " - FROM: " +  request.json['name'])
    else:
        print("RESPONDING TO: " + request.json['id'] +" - MSG: " + request.json['msg'] + " - FROM: " +  request.json['name'])
    return "ACK"

me = str(sys.argv[1])

def sending():
    while True:
        dest = ''
        id = ''
        reply = input("REPLY MESSAGE? (y or n): ")

        if (reply == 'y'):
            id = input("ENTER MESSAGE ID: ")
        dest = input("ENTER DESTINATION: ")
        msg = input("ENTER MESSAGE: ")

        data = {
            'dest':dest,
            'name':me,
            'msg':msg,
            'ip':const.registry[me][0],
            'id':id,
        }

        resposta = requests.post(const.CHAT_SERVER_HOST+":"+str(const.CHAT_SERVER_PORT)+'/chat', json = data)
        if resposta.text != "ACK":
            print("Error: Server did not accept the message (dest does not exist?)")
        else:
            pass

def receiving():
    app.run(host="0.0.0.0",port=const.registry[me][1])

if __name__ == '__main__':
    
    receive = threading.Thread(target=receiving)
    receive.start()

    send = threading.Thread(target=sending)
    send.start()