from flask import Flask, request, jsonify
import const 
import requests

count = 0
app = Flask(__name__)

@app.route('/chat',methods=['POST'])
def createChat():
    global count
    count +=1

    dados = {
        'dest':request.json['dest'],
        'remt':request.json['remt'],
        'msg':request.json['msg'],
        'id':request.json['id'],
        'count':count,
    }
    ip = const.registry[request.json['dest']][0]
    port = const.registry[request.json['dest']][1]

    print("FROM: " +  request.json['remt'] + " - TO: " +  request.json['dest'] + ' ID: ' +
        str(count) + " - RELAYING MSG: " + request.json['msg'] + '\n')
    resposta = requests.post(ip+":"+str(port)+'/chat', json = dados)
    return "ACK"

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=False)
