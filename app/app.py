#!/usr/bin/env python3

import os
import socket
import uuid

from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

#Ресурсный класс для эндпоинта /hostname
class Hostname(Resource):
    def get(self):
        try:
            if socket.getfqdn():
                return socket.getfqdn()
        except: 
            return 'Unable to get hostname'
        
#Ресурсный класс для эндпоинта /author
class Author(Resource):
    def get(self):
        return os.getenv('AUTHOR')

#Ресурсный класс для эндпоинта /id            
class Id(Resource):
    def get(self):        
        return str(uuid.UUID(os.environ['UUID']))
                  

api.add_resource(Hostname, '/hostname')
api.add_resource(Author, '/author')
api.add_resource(Id, '/id')

#Задание значения переменной окружения AUTHOR, если оно отсутствует
if not os.getenv('AUTHOR'):
    os.environ['AUTHOR']='deliowi'
    

#Проверка значения переменной окружения UUID и изменение значения, если оно некорректное или отсутствует
if os.getenv('UUID'):
    try:
        x = uuid.UUID(os.environ['UUID'])
    except:
        os.environ['UUID']=str(uuid.uuid4())
else:
    os.environ['UUID']=str(uuid.uuid4())


if __name__ == '__main__':
    app.run(port=8000, host='0.0.0.0')