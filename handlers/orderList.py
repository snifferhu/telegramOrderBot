# -*- coding: utf-8 -*-
import logging
from util.common import log_stream_handler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from handlers.callback_query import ol_callback

# 将定义好的console日志handler添加到root logger
logging.getLogger(__name__).addHandler(log_stream_handler())
logger = logging.getLogger(__name__)



def handle(bot, update):
    logger.info("chatId: %s,first_name: %s,text: %s", update.message.chat_id, update.message.from_user.first_name,
                update.message.text)
    from_user = update.message.from_user

    send_msg, keyboard_list = ol_callback.page(from_user.id, 1)
    if len(keyboard_list) == 0:
        bot.send_message(chat_id=update.message.from_user.id, text=send_msg)
    else:
        reply_markup = InlineKeyboardMarkup(keyboard_list)
        bot.send_message(chat_id=update.message.from_user.id, text=send_msg, reply_markup=reply_markup)

command = 'orderList'

from telegram.ext import CommandHandler

handler = CommandHandler(command, handle)
