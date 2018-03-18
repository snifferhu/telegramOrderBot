# -*- coding: utf-8 -*-
import logging
from util.common import log_stream_handler

# 将定义好的console日志handler添加到root logger
logging.getLogger(__name__).addHandler(log_stream_handler())
logger = logging.getLogger(__name__)
from handlers.callback import ll_callback,ol_callback
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from util.telegram_bot_util import default

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
    query_params = query.data.split("_")

    if query_params[0] == "ll":
        send_msg, keyboard_list = ll_callback.exec(query_params)
    elif query_params[0] == "bl":
        send_msg, keyboard_list = ll_callback.exec(query_params)
    elif query_params[0] == "ol":
        send_msg, keyboard_list = ol_callback.exec(query_params)
    else:
        send_msg, keyboard_list = default()
    reply_markup = InlineKeyboardMarkup(keyboard_list)
    bot.edit_message_text(text=send_msg,
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          reply_markup=reply_markup)


command = 'callback_query'

from telegram.ext import CallbackQueryHandler

handler = CallbackQueryHandler(callback_query)
