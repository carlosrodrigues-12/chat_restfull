
from flask import Flask
from flask import jsonify
from flask import request
import sys
import const 
import requests
import threading
# Handle interactive loop

app = Flask(__name__)

@app.route('/chat',methods=['POST'])
def createEmp():

    dados = {
    'dest':request.json['dest'],
    'name':request.json['name'],
    'msg':request.json['msg'],
    'id':request.json['id'],
    }
    #resposta = requests.post(dest_addr, data=data) #2
    if(request.json['id'] == ''):
        print(str(request.json['count']) + " - MSG: " + request.json['msg'] + " - FROM: " +  request.json['name']) # just print the message and destination
    else:
        print("RESPONDING TO: " + request.json['id'] +" - MSG: " + request.json['msg'] + " - FROM: " +  request.json['name']) # just print the message and destination
    return "ACK"

me = str(sys.argv[1]) # User's name (as registered in the registry. E.g., Alice, Bob, ...)

def sending():
    while True:
        dest = ''
        id = ''
        reply = input("REPLY? (y or n): \n")

        if (reply == 'y'):
            id = input("ENTER MESSAGE ID: \n")
        dest = input("ENTER DESTINATION: \n")
        msg = input("ENTER MESSAGE: \n")

        data = {
            'dest':dest,
            'name':me,
            'msg':msg,
            'ip':const.registry[me][0],
            'id':id,
        }

        # Send message and wait for confirmation
        resposta = requests.post(const.CHAT_SERVER_HOST+":"+str(const.CHAT_SERVER_PORT)+'/chat', json = data) #2
        if resposta.text != "ACK":
            print("Error: Server did not accept the message (dest does not exist?)")
        else:
            #print("Received Ack from server")
            pass

def receiving():
    app.run(host="0.0.0.0",port=const.registry[me][1])

if __name__ == '__main__':
    
    send = threading.Thread(target=sending)
    send.start()
    
    receive = threading.Thread(target=receiving)
    receive.start()