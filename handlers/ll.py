# -*- coding: utf-8 -*-
import logging
from util.common import log_stream_handler
from handlers.callback import ll_callback
from telegram import InlineKeyboardMarkup

# 将定义好的console日志handler添加到root logger
logging.getLogger(__name__).addHandler(log_stream_handler())
logger = logging.getLogger(__name__)




def ll(bot, update):
    logger.info("chatId: %s,first_name: %s,text: %s",
                update.message.chat_id,
                update.message.from_user.first_name,
                update.message.text)

    send_msg, keyboard_list = ll_callback.page("0", 1)
    reply_markup = InlineKeyboardMarkup(keyboard_list)
    bot.send_message(chat_id=update.message.from_user.id, text=send_msg, reply_markup=reply_markup)


command = 'll'

from telegram.ext import CommandHandler

handler = CommandHandler(command, ll)
