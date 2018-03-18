# -*- coding: utf-8 -*-
import logging
from util.common import log_stream_handler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# 将定义好的console日志handler添加到root logger
logging.getLogger(__name__).addHandler(log_stream_handler())
logger = logging.getLogger(__name__)

from service import order_service
prefix = 'ol'

def gen_keyboard():
    return [[InlineKeyboardButton("1", callback_data='ol_page_1_0'),
             InlineKeyboardButton("2", callback_data='ol_page_2_0'),
             InlineKeyboardButton("3", callback_data='ol_page_3_0'),
             InlineKeyboardButton("4", callback_data='ol_page_4_0'),
             InlineKeyboardButton("next", callback_data='ol_next_1_0')],

            [InlineKeyboardButton("close", callback_data='ol_close')]
            ]


def handle(bot, update):
    logger.info("chatId: %s,first_name: %s,text: %s", update.message.chat_id, update.message.from_user.first_name,
                update.message.text)
    from_user = update.message.from_user
    count = order_service.select_count_teleId(from_user.id)
    logger.info(count)
    send_msg = order_service.select_by_teleId(from_user.id)
    bot.send_message(chat_id=update.message.from_user.id, text=send_msg)


command = 'orderList'

from telegram.ext import CommandHandler

handler = CommandHandler(command, handle)
