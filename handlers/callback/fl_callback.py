# -*- coding: utf-8 -*-
import logging
from util.common import log_stream_handler

# 将定义好的console日志handler添加到root logger
logging.getLogger(__name__).addHandler(log_stream_handler())
logger = logging.getLogger(__name__)

from service import balance_service
from telegram import InlineKeyboardButton
from util.telegram_bot_util import create_page_button_list
from util.common import page_number
from util.telegram_bot_util import close, default

prefix = 'fl'

close_button = [InlineKeyboardButton("close", callback_data='fl_close')]


def gen_order_keyboard(order):
    return [InlineKeyboardButton("Order Id" if order[0] != "member_id" else "[ Order Id ]",
                                 callback_data='fl_order_{0}'.format(order[1][0])),
            InlineKeyboardButton("Order Name" if order[0] != "nick_name" else "[ Order Name ]",
                                 callback_data='fl_order_{0}'.format(order[1][1])),
            InlineKeyboardButton("Order Money" if order[0] != "amount" else "[ Order Money ]",
                                 callback_data='fl_order_{0}'.format(order[1][2]))]


order_flied_dict = {
    "ida": ["member_id", ["idd", "named", "amd"], "asc"],
    "idd": ["member_id", ["ida", "namea", "ama"], "desc"],
    "namea": ["nick_name", ["idd", "named", "amd"], "asc"],
    "named": ["nick_name", ["ida", "namea", "ama"], "desc"],
    "ama": ["amount", ["idd", "named", "amd"], "asc"],
    "amd": ["amount", ["ida", "namea", "ama"], "desc"]
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
    elif query_params[1] == "current":
        order = query_params[3]
        current_page = int(query_params[2].replace('[', '').replace(']', '').strip())
        msg_hash = query_params[4]
        return current(from_user.id, order, current_page, msg_hash)
    else:
        return default()


def page(tele_id, order, current_page, send_msg=None):
    count = balance_service.select_count_driver_teleId(tele_id)
    if send_msg == None:
        send_msg = balance_service.select_by_driver_teleId(tele_id,
                                                           current_page,
                                                           order_flied_dict[order][0],
                                                           order_flied_dict[order][2])

    keyboard_list = []
    if count != 0 and int(count) > page_number:
        keyboard_order = gen_order_keyboard(order_flied_dict[order])
        keyboard_list.append(keyboard_order)

        keyboard_page = create_page_button_list(send_msg, count, prefix, current_page, order)
        keyboard_list.append(keyboard_page)
        keyboard_list.append(close_button)
    return send_msg, keyboard_list


def current(tele_id, order, current_page, msg_hash):
    send_msg = balance_service.select_by_driver_teleId(tele_id,
                                                       current_page,
                                                       order_flied_dict[order][0],
                                                       order_flied_dict[order][2])
    if int(msg_hash) != hash(send_msg):
        return page(tele_id, order, current_page, send_msg)
    return '', []
