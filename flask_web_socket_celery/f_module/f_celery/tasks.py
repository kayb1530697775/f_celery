# -*- coding:utf-8 -*-
# @Time   : 12/8/19 12:14 AM
# @Author : Kayb

import time
import requests
from common import socket_box

from f_module.f_celery.celery_manager import c_app


@c_app.task
def add(x, y):
    time.sleep(5)
    return x+y


@c_app.task
def send_request_msg():
    response = requests.get(url="http://127.0.0.1:5000/accept_asyn_meg/")
    return response.status_code
