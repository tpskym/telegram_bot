import os
import requests
from flask import Flask, request, Response
import json

app = Flask(__name__)



# def RequestItilium(dict_data):
#     print("thread:" + GetCurrentThread() + "stack: RequestItilium")
#     try:
#        quote = "\""
#        response = requests.post(address_api_itilium, data=json.dumps(dict_data).encode('utf-8'),
#                             auth=(login_itilium, password_itilium))
#        code = response.status_code
#        description = response.text
#        print("thread:" + GetCurrentThread() + "  code: " + str(code))
#        print("thread:" + GetCurrentThread() + "  description: " + description)
#        if (code == 200):
#            return False, description, True
#        else:
#            return False, str(code) + ' ' + description, False
#     except:
#        return True, "Ошибка соединения с Итилиум. Обратитесь к администратору.", False


@app.route('/getWebhookInfo',  methods=['GET'])
def getWebHookInfo():
    ret = requests.post("https://api.telegram.org/bot" + os.environ['AUTH_KEY_BOT'] + "/getWebhookInfo")
    return ret.text

@app.route('/setWebHook',  methods=['GET'])
def setWebHook():
    dict_data = dict()
    address = request.url.replace("setWebHook",os.environ['AUTH_KEY_BOT'])
    print(address)
    dict_data.update( {"url": address} )
    
    print(dict_data)
    
    ret = requests.post("https://api.telegram.org/bot" + os.environ['AUTH_KEY_BOT'] + "/setWebhook", 
        data = json.dumps(dict_data).encode('utf-8'), 
        headers = {"Content-Type" : "application/json"})
    
    
    return ret.text
    

@app.route('/removeWebHook',  methods=['GET'])
def removeWebHook():
    dict_data = dict()
    dict_data.update( {"url": ""} )
    
    ret = requests.post("https://api.telegram.org/bot" + os.environ['AUTH_KEY_BOT'] + "/setWebhook", 
        data = json.dumps(dict_data).encode('utf-8'), 
        headers = {"Content-Type" : "application/json"})
    
    return ret.text

# @app.route('/' + os.environ['AUTH_KEY_BOT'],  methods=['GET'])
# def test():
#     print("rrrrrr")
#     return "sdsd"

@app.route('/' + os.environ['AUTH_KEY_BOT'],  methods=['POST'])
def IncomingConnectionPost():
    print("new message")
    return Response(status=200)



