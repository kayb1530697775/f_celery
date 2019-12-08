# -*- coding:utf-8 -*-
# @Time   : 12/6/19 11:35 PM
# @Author : Kayb

from flask import Flask
from flask_sockets import Sockets


app = Flask(__name__)
socket_app = Sockets(app)


from apps import apps_bp, ws_bp


app.register_blueprint(apps_bp)
socket_app.register_blueprint(ws_bp)

if __name__ == '__main__':
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    server = pywsgi.WSGIServer(('0.0.0.0', 5000), app, handler_class=WebSocketHandler)
    print('server start')
    server.serve_forever()

