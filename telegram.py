import requests
from flask import Flask, request, Response
import json


def test():
    auth_key = os.environ['DATABASE_URL']


def RequestItilium(dict_data):
    print("thread:" + GetCurrentThread() + "stack: RequestItilium")
    try:
       quote = "\""
       response = requests.post(address_api_itilium, data=json.dumps(dict_data).encode('utf-8'),
                            auth=(login_itilium, password_itilium))
       code = response.status_code
       description = response.text
       print("thread:" + GetCurrentThread() + "  code: " + str(code))
       print("thread:" + GetCurrentThread() + "  description: " + description)
       if (code == 200):
           return False, description, True
       else:
           return False, str(code) + ' ' + description, False
    except:
       return True, "Ошибка соединения с Итилиум. Обратитесь к администратору.", False



@app.route('/',  methods=['POST'])
def IncomingConnectionPost(parameter_list):
    raise NotImplementedError


def f():
    reise NotImplementedError 
