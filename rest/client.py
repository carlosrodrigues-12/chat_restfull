from time import sleep
from flask import Flask, request, jsonify
import sys
import const 
import requests
import threading

count = 0
app = Flask(__name__)

@app.route('/chat',methods=['POST'])
def createChat():
    global count
    count+=1

    dados = {
        'dest':request.json['dest'],
        'remt':request.json['remt'],
        'msg':request.json['msg'],
        'id':request.json['id'],
    }

    if(request.json['id'] == ''):
        print("FROM: " +  request.json['remt'] + ' ID: ' + str(request.json['count']) + " - MSG: " + request.json['msg'])
    else:
        print("FROM: " +  request.json['remt'] + " - RESPONDING TO: " + request.json['id'] +
        " - MSG: " + request.json['msg'])
    return "ACK"

def send():
    while True:
        global count
        dest = ''
        id = ''
        reply = 'n'
        if count>0:
            reply = input("REPLY MESSAGE? (y or n): ")

        if (reply == 'y'):
            id = input("ENTER MESSAGE ID: ")
        dest = input("ENTER DESTINATION: ")
        msg = input("ENTER MESSAGE: ")

        data = {
            'dest':dest,
            'remt':me,
            'msg':msg,
            'ip':const.registry[me][0],
            'id':id,
        }

        resposta = requests.post(const.CHAT_SERVER_HOST+":"+str(const.CHAT_SERVER_PORT)+'/chat', json = data)
        if resposta.text != "ACK":
            print("Error: Server did not accept the message (dest does not exist?)")
        else:
            pass

def recv():
    app.run(host="0.0.0.0",port=const.registry[me][1],debug=False)

me = str(sys.argv[1])

if __name__ == '__main__':
    
    r = threading.Thread(target=recv)
    r.start()
    sleep(2)
    s = threading.Thread(target=send)
    s.start()