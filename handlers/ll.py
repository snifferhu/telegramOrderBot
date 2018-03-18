# -*- coding: utf-8 -*-
import logging
from util.common import log_stream_handler

# 将定义好的console日志handler添加到root logger
logging.getLogger(__name__).addHandler(log_stream_handler())
logger = logging.getLogger(__name__)

from service import order_service
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

prefix = 'll'

pre_button = InlineKeyboardButton("pre", callback_data='ll_pre_1_0')
close_button = [InlineKeyboardButton("close", callback_data='ll_close')]

def gen_status_keyboard():
    return [InlineKeyboardButton("Init", callback_data='ll_status_0'),
             InlineKeyboardButton("Cancel", callback_data='ll_status_1'),
             InlineKeyboardButton("Over", callback_data='ll_status_2'),
             InlineKeyboardButton("Receive", callback_data='ll_status_3')]

def gen_keyboard():
    return [[InlineKeyboardButton("Init", callback_data='ll_status_0'),
             InlineKeyboardButton("Cancel", callback_data='ll_status_1'),
             InlineKeyboardButton("Over", callback_data='ll_status_2'),
             InlineKeyboardButton("Receive", callback_data='ll_status_3')],

            [InlineKeyboardButton("1", callback_data='ll_page_1_0'),
             InlineKeyboardButton("2", callback_data='ll_page_2_0'),
             InlineKeyboardButton("3", callback_data='ll_page_3_0'),
             InlineKeyboardButton("4", callback_data='ll_page_4_0'),
             InlineKeyboardButton("next", callback_data='ll_next_1_0')],

            [InlineKeyboardButton("close", callback_data='ll_close')]
            ]


def ll(bot, update):
    logger.info("chatId: %s,first_name: %s,text: %s",
                update.message.chat_id,
                update.message.from_user.first_name,
                update.message.text)


    count = order_service.select_count_status("0")
    send_msg = order_service.select_by_status("0")

    keyboard = gen_keyboard()
    if count == 0 or int(count) < 11:
        keyboard.remove(keyboard[1])
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.send_message(chat_id=update.message.from_user.id, text=send_msg, reply_markup=reply_markup)


command = 'll'

from telegram.ext import CommandHandler

handler = CommandHandler(command, ll)
