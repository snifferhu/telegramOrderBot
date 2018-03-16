# -*- coding: utf-8 -*-
import logging
from util.common import log_stream_handler

# 将定义好的console日志handler添加到root logger
logging.getLogger(__name__).addHandler(log_stream_handler())
logger = logging.getLogger(__name__)

from util.common import order_status
from dao import order_info_dao
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

STATUS, PAGE = range(2)

pre_button = InlineKeyboardButton("pre", callback_data='pre')

keyboard = [[InlineKeyboardButton("Init", callback_data='0'),
             InlineKeyboardButton("Cancel", callback_data='1'),
             InlineKeyboardButton("Over", callback_data='2'),
             InlineKeyboardButton("Receive", callback_data='3')],

            [InlineKeyboardButton("1", callback_data='p1'),
             InlineKeyboardButton("2", callback_data='p2'),
             InlineKeyboardButton("3", callback_data='p3'),
             InlineKeyboardButton("next", callback_data='next')],

            [InlineKeyboardButton("over", callback_data='over')]
            ]


def callback_query(bot, update):
    query = update.callback_query
    logger.info(query)
    reply_markup = InlineKeyboardMarkup(keyboard)
    orders = order_info_dao.select_by_status(query.data)
    from util.common import order_title_msg
    from util.common import order_info_msg
    send_msg = "" + order_title_msg
    for order in orders:
        send_msg = send_msg + order_info_msg.format(order['id'],
                                                    order['item'],
                                                    order['price'],
                                                    order['create_time'],
                                                    order_status[order['order_status']])
    bot.edit_message_text(text=send_msg,
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          reply_markup=reply_markup)
    # bot.send_message(chat_id=update.message.from_user.id, text=send_msg, reply_markup=reply_markup)


command = 'callback_query'

from telegram.ext import CallbackQueryHandler

handler = CallbackQueryHandler(callback_query)
