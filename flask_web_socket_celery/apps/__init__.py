# -*- coding:utf-8 -*-
# @Time   : 12/6/19 11:50 PM
# @Author : Kayb

from flask import Blueprint

from .indexs import index, view_all_socket, send_message, trigger_aysn_task, accept_asyn_meg
from .connect_wb import connect_wb

apps_bp = Blueprint('apps', __name__)
ws_bp = Blueprint('ws_apps', __name__)

apps_bp.add_url_rule('/', view_func=index)  # index
apps_bp.add_url_rule('/view_all_socket/', view_func=view_all_socket)  # view all socket
apps_bp.add_url_rule('/send_msg/', view_func=send_message)  # send messae
apps_bp.add_url_rule('/trigger_aysn_task/', view_func=trigger_aysn_task)  # trigger aysn task
apps_bp.add_url_rule('/accept_asyn_meg/', view_func=accept_asyn_meg)  # accept aysn meg
ws_bp.add_url_rule('/connect_wb/', view_func=connect_wb)  # connect websocket


