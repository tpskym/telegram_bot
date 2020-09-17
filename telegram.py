import os
import requests
from flask import Flask, request, Response
import json

app = Flask(__name__)

def test():
    auth_key = os.environ['AUTH_KEY_BOT']


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
def getWwebHookInfo():
    ret = requests.post("https://api.telegram.org/bot" + os.environ['AUTH_KEY_BOT'] + "/getWebhookInfo")
    return ret.text

@app.route('/setWebHook',  methods=['GET'])
def setWeebHook():
    dict_data = dict()
    address = request.url.replace("setWebHook",os.environ['AUTH_KEY_BOT'])
    print(address)
    dict_data.update( {"url": address} )
    ret = requests.post("https://api.telegram.org/bot" + os.environ['AUTH_KEY_BOT'] + "/setWebhook", data = json.dumps(dict_data).encode('utf-8'))
    
    return ret.text
    

@app.route('/' + os.environ['AUTH_KEY_BOT'],  methods=['GET'])
def test():
    print("rrrrrr")

@app.route('/' + os.environ['AUTH_KEY_BOT'],  methods=['POST'])
def IncomingConnectionPost(parameter_list):
    print("new message")


