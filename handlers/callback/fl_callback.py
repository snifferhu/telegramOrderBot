# -*- coding: utf-8 -*-
import logging
from util.common import log_stream_handler

# 将定义好的console日志handler添加到root logger
logging.getLogger(__name__).addHandler(log_stream_handler())
logger = logging.getLogger(__name__)

from service import deposit_service, balance_service
from telegram import InlineKeyboardButton
from util.telegram_bot_util import create_page_button_list
from util.common import page_number
from util.telegram_bot_util import close, default

prefix = 'fl'

close_button = [InlineKeyboardButton("close", callback_data='fl_close')]


def gen_order_keyboard(order):
    return [InlineKeyboardButton("Order Id" if order != "id" else "[ Order Id ]", callback_data='fl_order_id'),
            InlineKeyboardButton("Order Name" if order != "name" else "[ Order Name ]", callback_data='fl_order_name'),
            InlineKeyboardButton("Order Money" if order != "am" else "[ Order Money ]", callback_data='fl_order_am')]


order_flied_dict = {
    "id": "member_id",
    "name": "nick_name",
    "am": "amount"
}


def exec(from_user, query_params):
    logger.info(query_params)
    if query_params[1] == "order":
        order = query_params[2]
        current_page = 1
        return page(from_user.id, order, current_page)
    elif query_params[1] == "next" or query_params[1] == "page" or query_params[1] == "pre":
        order = query_params[3]
        current_page = int(query_params[2])
        return page(from_user.id, order, current_page)
    elif query_params[1] == "close":
        return close()
    else:
        return default()


def page(tele_id, order, current_page):
    count = balance_service.select_count_driver_teleId(tele_id)
    send_msg = balance_service.select_by_driver_teleId(tele_id, current_page, order_flied_dict[order])

    keyboard_list = []
    if count != 0 and int(count) > page_number:
        keyboard_order = gen_order_keyboard([order])
        keyboard_list.append(keyboard_order)

        keyboard_page = create_page_button_list(count, prefix, current_page, tele_id)
        keyboard_list.append(keyboard_page)
        keyboard_list.append(close_button)
    return send_msg, keyboard_list
