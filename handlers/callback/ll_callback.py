# -*- coding: utf-8 -*-
import logging
from util.common import log_stream_handler

# 将定义好的console日志handler添加到root logger
logging.getLogger(__name__).addHandler(log_stream_handler())
logger = logging.getLogger(__name__)

from service import order_service
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from util.telegram_bot_util import create_page_button_list
from util.common import page_number
from util.telegram_bot_util import close

prefix = 'll'

close_button = [InlineKeyboardButton("close", callback_data='ll_close')]


def gen_status_keyboard():
    return [InlineKeyboardButton("Init", callback_data='ll_status_0'),
            InlineKeyboardButton("Cancel", callback_data='ll_status_1'),
            InlineKeyboardButton("Over", callback_data='ll_status_2'),
            InlineKeyboardButton("Receive", callback_data='ll_status_3')]


def exec(query_params):
    logger.info(query_params)
    if query_params[1] == "status":
        status = query_params[2]
        current_page = 1
        return page(status, current_page)
    elif query_params[1] == "next" or query_params[1] == "page" or query_params[1] == "pre":
        status = query_params[3]
        current_page = int(query_params[2])
        return page(status, current_page)
    elif query_params[1] == "close":
        return close()
    else:
        from handlers.callback_query import default
        return default()


def page(status, current_page):
    count = order_service.select_count_status(status)
    send_msg = order_service.select_by_status(status, current_page)

    keyboard_list = []
    keyboard_status = gen_status_keyboard()
    keyboard_list.append(keyboard_status)

    if count != 0 and int(count) > page_number:
        keyboard_page = create_page_button_list(count, prefix, current_page, status)
        keyboard_list.append(keyboard_page)
    keyboard_list.append(close_button)
    return send_msg, keyboard_list
