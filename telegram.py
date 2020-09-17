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


@app.route('/setWebHook',  methods=['GET'])
def setWeebHook():
    # dict_data = dict()
    # address = request.url.replace("setWebHook","")
    # print(address)
    # dict_data.update( {"url": address} )
    
    # requests.post("https://api.telegram.org/bot" + os.environ['AUTH_KEY_BOT'] + "/", data = json.dumps(dict_data).encode('utf-8'))
    print("end")
    



@app.route('/',  methods=['POST'])
def IncomingConnectionPost(parameter_list):
    print("new message")


