# -*- coding: utf-8 -*-
import logging

from dao import member_dao
from util.common import log_stream_handler

# 将定义好的console日志handler添加到root logger
logging.getLogger(__name__).addHandler(log_stream_handler())
logger = logging.getLogger(__name__)

from service import order_service, member_service
from telegram import InlineKeyboardButton
from util.telegram_bot_util import create_page_button_list
from util.common import page_number
from util.telegram_bot_util import close, default

prefix = 'll'

close_button = [InlineKeyboardButton("close", callback_data='ll_close')]


def gen_status_keyboard(status, send_msg):
    return [InlineKeyboardButton("Init" if status != "0" else "[ Init ]",
                                 callback_data='ll_status_0_{}'.format(hash(send_msg))),
            InlineKeyboardButton("Cancel" if status != "1" else "[ Cancel ]",
                                 callback_data='ll_status_1_{}'.format(hash(send_msg))),
            InlineKeyboardButton("Over" if status != "2" else "[ Over ]",
                                 callback_data='ll_status_2_{}'.format(hash(send_msg))),
            InlineKeyboardButton("Receive" if status != "3" else "[ Receive ]",
                                 callback_data='ll_status_3_{}'.format(hash(send_msg)))]


def exec(from_user, query_params):
    logger.info(query_params)
    if query_params[1] == "status":
        status = query_params[2]
        current_page = 1
        msg_hash = query_params[3]
        return current(from_user, status, current_page, msg_hash)
    elif query_params[1] == "next" or query_params[1] == "page" or query_params[1] == "pre":
        status = query_params[3]
        current_page = int(query_params[2])
        return page(from_user, status, current_page)
    elif query_params[1] == "close":
        return close()
    elif query_params[1] == "current":
        status = query_params[3]
        current_page = int(query_params[2].replace('[', '').replace(']', '').strip())
        msg_hash = query_params[4]
        return current(from_user, status, current_page, msg_hash)
    else:
        return default()


def page(from_user, status, current_page, send_msg=None, member=None):
    if member == None:
        member = member_service.select_by_tele_id(from_user)
    count = order_service.select_count_status(status, member[0]['driver_id'])
    if send_msg == None:
        send_msg = order_service.select_by_status(status, current_page, member[0]['driver_id'])

    keyboard_list = []
    keyboard_status = gen_status_keyboard(status, send_msg)
    keyboard_list.append(keyboard_status)

    if count != 0 and int(count) > page_number:
        keyboard_page = create_page_button_list(send_msg, count, prefix, current_page, status)
        keyboard_list.append(keyboard_page)
    keyboard_list.append(close_button)
    return send_msg, keyboard_list


def current(from_user, status, current_page, msg_hash):
    member = member_service.select_by_tele_id(from_user)
    send_msg = order_service.select_by_status(status, current_page, member[0]['driver_id'])
    if int(msg_hash) != hash(send_msg):
        return page(from_user, status, current_page, send_msg, member)
    return '', []
