# -*- coding: utf-8 -*-
import logging
from util.common import log_stream_handler

# 将定义好的console日志handler添加到root logger
logging.getLogger(__name__).addHandler(log_stream_handler())
logger = logging.getLogger(__name__)

from service import deposit_service
from dao import member_dao
from telegram import InlineKeyboardButton
from util.telegram_bot_util import create_page_button_list
from util.common import page_number
from util.telegram_bot_util import close, default

prefix = 'dl'

close_button = [InlineKeyboardButton("close", callback_data='dl_close')]


def exec(query_params):
    logger.info(query_params)
    if query_params[1] == "next" or query_params[1] == "page" or query_params[1] == "pre":
        current_page = int(query_params[2])
        return page(current_page)
    elif query_params[1] == "close":
        return close()
    elif query_params[1] == "current":
        current_page = int(query_params[2].replace('[', '').replace(']', '').strip())
        msg_hash = query_params[4]
        return current(current_page, msg_hash)
    else:
        return default()


def page(current_page, send_msg=None):
    count = deposit_service.select_count_driverId()
    if send_msg == None:
        send_msg = deposit_service.select_by_driverId(current_page)
    keyboard_list = []
    if count != 0 and int(count) > page_number:
        keyboard_page = create_page_button_list(send_msg, count, prefix, current_page, '-1')
        keyboard_list.append(keyboard_page)
        keyboard_list.append(close_button)
    return send_msg, keyboard_list


def current(current_page, msg_hash):
    send_msg = deposit_service.select_count_driverId()
    if int(msg_hash) != hash(send_msg):
        return page(current_page, send_msg)
    return '', []
