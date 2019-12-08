# -*- coding:utf-8 -*-
# @Time   : 12/6/19 11:47 PM
# @Author : Kayb

from flask import render_template
from common import socket_box
from f_module.f_celery.tasks import send_request_msg


# upload index
def index():
    return render_template('index.html')


# view all socket
def view_all_socket():
    print(socket_box)
    return 'ok'


# send message
def send_message():
    for socket in socket_box:
        socket.send('send test message')

    return 'send success'


# trigger aysn task
def trigger_aysn_task():
    send_request_msg.apply_async(countdown=10)
    return 'aysn task success'


# send socket meg
def accept_asyn_meg():
    msg = 'hint mark'
    for socket in socket_box:
        socket.send(msg)
    return 'ok'