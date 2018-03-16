# -*- coding: utf-8 -*-
import logging
from util.common import log_stream_handler

# 将定义好的console日志handler添加到root logger
logging.getLogger(__name__).addHandler(log_stream_handler())
logger = logging.getLogger(__name__)

from util.common import order_status
from dao import order_info_dao
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from util.telegram_bot_util import *

def ol(bot, update):
    query = update.callback_query
    logger.info(query)
    query_data_list = query.data.split("_")
    if query_data_list[1].isdigit():
        logger.info("")
    elif query_data_list[1] == "pre":
        logger.info("")
    elif query_data_list[1] == "next":
        logger.info("")
    elif query_data_list[1] == "over":
        logger.info("")
        over(bot, query)
    # count = order_info_dao.select_count_teleId(query.from_id)
    # page = count / 10 + count % 10 == 0 if 0 else 1
    # create_page_button_list
    # reply_markup = InlineKeyboardMarkup(keyboard)
    # orders = order_info_dao.select_by_status(query.data)
    # from util.common import order_title_msg
    # from util.common import order_info_msg
    # send_msg = "" + order_title_msg
    # for order in orders:
    #     send_msg = send_msg + order_info_msg.format(order['id'],
    #                                                 order['item'],
    #                                                 order['price'],
    #                                                 order['create_time'],
    #                                                 order_status[order['order_status']])
    # bot.edit_message_text(text=send_msg,
    #                       chat_id=query.message.chat_id,
    #                       message_id=query.message.message_id,
    #                       reply_markup=reply_markup)
    # bot.send_message(chat_id=update.message.from_user.id, text=send_msg, reply_markup=reply_markup)


def over(bot, query):
    bot.edit_message_text(text="Selected option: {}".format(query.data),
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id)


command = 'ol_sub_callback_query'

from telegram.ext import CallbackQueryHandler

handler = CallbackQueryHandler(ol)
