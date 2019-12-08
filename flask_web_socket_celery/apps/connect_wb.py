# -*- coding:utf-8 -*-
# @Time   : 12/7/19 1:33 AM
# @Author : Kayb

from flask import request
from common import socket_box


def connect_wb(socket):
    socket_box.append(socket)
    while not socket.closed:
        a = request
        print(a)
        msg = socket.receive()
        if msg is None:
            try:
                socket_box.remove(socket)
            except Exception as e:
                pass



