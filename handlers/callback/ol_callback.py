# -*- coding: utf-8 -*-
import logging
from util.common import log_stream_handler

# 将定义好的console日志handler添加到root logger
logging.getLogger(__name__).addHandler(log_stream_handler())
logger = logging.getLogger(__name__)

from service import order_service
from telegram import InlineKeyboardButton
from util.telegram_bot_util import create_page_button_list
from util.common import page_number
from util.telegram_bot_util import close, default

prefix = 'ol'

close_button = [InlineKeyboardButton("close", callback_data='ol_close')]


def exec(query_params):
    logger.info(query_params)
    if query_params[1] == "next" or query_params[1] == "page" or query_params[1] == "pre":
        tele_id = query_params[3]
        current_page = int(query_params[2])
        return page(tele_id, current_page)
    elif query_params[1] == "close":
        return close()
    else:
        return default()


def page(tele_id, current_page):
    count = order_service.select_count_teleId(tele_id)
    send_msg = order_service.select_by_teleId(tele_id, current_page)

    keyboard_list = []

    if count != 0 and int(count) > page_number:
        keyboard_page = create_page_button_list(count, prefix, current_page, tele_id)
        keyboard_list.append(keyboard_page)
        keyboard_list.append(close_button)
    return send_msg, keyboard_list
