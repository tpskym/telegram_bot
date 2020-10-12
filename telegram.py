import os
import requests
from flask import Flask, request, Response
import json

app = Flask(__name__)

address_api_itilium = os.environ['AddressApiItilium']
login_itilium = os.environ['LoginItilium']
password_itilium = os.environ['PasswordItilium']
auth_key =  os.environ['AuthKey'] 


@app.route('/getWebhookInfo',  methods=['GET'])
def getWebHookInfo():
    # это только на время теста, надо скрывать в продакшене
    ret = requests.post("https://api.telegram.org/bot" + auth_key + "/getWebhookInfo")
    return ret.text

@app.route('/setWebHook',  methods=['GET'])
def setWebHook():
    dict_data = dict()
    address = request.url.replace("setWebHook",auth_key)
    print(address)
    dict_data.update( {"url": address} )
    
    print(dict_data)
    
    ret = requests.post("https://api.telegram.org/bot" + auth_key + "/setWebhook", 
        data = json.dumps(dict_data).encode('utf-8'), 
        headers = {"Content-Type" : "application/json"})
    
    
    return ret.text
    

@app.route('/removeWebHook',  methods=['GET'])
def removeWebHook():
    dict_data = dict()
    dict_data.update( {"url": ""} )
    
    ret = requests.post("https://api.telegram.org/bot" + auth_key + "/setWebhook", 
        data = json.dumps(dict_data).encode('utf-8'), 
        headers = {"Content-Type" : "application/json"})
    
    return ret.text


@app.route('/' + auth_key,  methods=['POST'])
def IncomingConnectionPost():
    print("new message")
    return Response(status=200)



