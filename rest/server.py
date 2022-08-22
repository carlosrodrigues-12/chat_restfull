
from flask import Flask
from flask import jsonify
from flask import request
import const 
import requests

app = Flask(__name__)


print("Chat Server is ready...")


count = 0

@app.route('/chat',methods=['POST'])
def createEmp():
    global count
    count +=1
    
    dados = {
    'dest':request.json['dest'],
    'name':request.json['name'],
    'msg':request.json['msg'],
    'id':request.json['id'],
    'count':count,
    }
    ip = const.registry[request.json['dest']][0]
    port = const.registry[request.json['dest']][1]


    #resposta = requests.post(dest_addr, data=data) #2
    print(str(count) + " - RELAYING MSG: " + request.json['msg'] + " - FROM: " +  request.json['name'] + " - TO: " +  request.json['dest'] + '\n') # just print the message and destination
    resposta = requests.post(ip+":"+str(port)+'/chat', json = dados) #2
    return "ACK"

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)