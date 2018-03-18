# -*- coding: utf-8 -*-
import logging
from util.common import log_stream_handler

# 将定义好的console日志handler添加到root logger
logging.getLogger(__name__).addHandler(log_stream_handler())
logger = logging.getLogger(__name__)

from service import order_service
from handlers.ll import gen_status_keyboard
from handlers.ll import prefix
from telegram import InlineKeyboardMarkup
from util.telegram_bot_util import create_page_button_list
from util.telegram_bot_util import create_close_button
from handlers.ll import close_button


def exec(query_params, bot, update):
    logger.info(query_params)
    if query_params[1] == "status":
        status(query_params, bot, update)
    elif query_params[1] == "next":
        next(query_params, bot, update)
    elif query_params[1] == "close":
        close(bot, update)
    elif query_params[1] == "page":
        page(query_params, bot, update)
    elif query_params[1] == "pre":
        pre(query_params, bot, update)


def status(query_params, bot, update):
    status = query_params[2]
    pageIndex = 1
    count = order_service.select_count_status(status)
    send_msg = order_service.select_by_status(status)
    query = update.callback_query

    keyboard_list = []
    keyboard_status = gen_status_keyboard()
    keyboard_list.append(keyboard_status)
    if count != 0 and int(count) > 10:
        keyboard_page = create_page_button_list(count, prefix, pageIndex, status)
        keyboard_list.append(keyboard_page)
    keyboard_list.append(close_button)
    reply_markup = InlineKeyboardMarkup(keyboard_list)
    bot.edit_message_text(text=send_msg,
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          reply_markup=reply_markup)


def next(query_params, bot, update):
    status = query_params[3]
    next_page = int(query_params[2])
    count = order_service.select_count_status(status)
    send_msg = order_service.select_by_status(status, next_page)
    query = update.callback_query

    keyboard_list = []
    keyboard_status = gen_status_keyboard()
    keyboard_list.append(keyboard_status)

    keyboard_page = create_page_button_list(count, prefix, next_page, status)
    keyboard_list.append(keyboard_page)
    keyboard_list.append(close_button)
    reply_markup = InlineKeyboardMarkup(keyboard_list)
    bot.edit_message_text(text=send_msg,
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          reply_markup=reply_markup)

def pre(query_params, bot, update):
    status = query_params[3]
    pre_page = int(query_params[2])
    count = order_service.select_count_status(status)
    send_msg = order_service.select_by_status(status, pre_page)
    query = update.callback_query

    keyboard_list = []
    keyboard_status = gen_status_keyboard()
    keyboard_list.append(keyboard_status)

    keyboard_page = create_page_button_list(count, prefix, pre_page, status)
    keyboard_list.append(keyboard_page)
    keyboard_list.append(close_button)
    reply_markup = InlineKeyboardMarkup(keyboard_list)
    bot.edit_message_text(text=send_msg,
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          reply_markup=reply_markup)

def close(bot, update):
    bot.edit_message_text(text='再见! 期待下一次的合作.',
                          chat_id=update.callback_query.message.chat_id,
                          message_id=update.callback_query.message.message_id,
                          reply_markup=InlineKeyboardMarkup([]))


def page(query_params, bot, update):
    status = query_params[3]
    current_page = int(query_params[2])
    count = order_service.select_count_status(status)
    send_msg = order_service.select_by_status(status, current_page)
    query = update.callback_query

    keyboard_list = []
    keyboard_status = gen_status_keyboard()
    keyboard_list.append(keyboard_status)

    keyboard_page = create_page_button_list(count, prefix, current_page, status)
    keyboard_list.append(keyboard_page)
    keyboard_list.append(close_button)
    reply_markup = InlineKeyboardMarkup(keyboard_list)
    bot.edit_message_text(text=send_msg,
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          reply_markup=reply_markup)
