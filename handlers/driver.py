# -*- coding: utf-8 -*-
import logging
from util.common import log_stream_handler

# 将定义好的console日志handler添加到root logger
logging.getLogger(__name__).addHandler(log_stream_handler())
logger = logging.getLogger(__name__)

from util.common import role_send_text
from util.common import parse_cmd
from service import member_service
from util.common import balance_send_text

from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)

DOING, DONE = range(2)


def driver(bot, update):
    logger.info("chatId: %s,first_name: %s,text: %s", update.message.chat_id, update.message.from_user.first_name,
                update.message.text)
    from_user = update.message.from_user
    reply_keyboard = [['Yes', 'No']]
    from util.common import driver_start_text
    bot.send_message(chat_id=from_user.id,
                     text=driver_start_text.format(from_user.first_name),
                     reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return DOING


def doing(bot, update):
    cmd, text = parse_cmd(update.message.text)
    from_user = update.message.from_user
    logger.info(update.message.text)
    bot.send_message(chat_id=from_user.id,
                     text=text,
                     reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END


def cancel(bot, update):
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text('再见! 期待下一次的合作.',
                              reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END


command = 'driver'

from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler)

handler = ConversationHandler(
    entry_points=[CommandHandler(command, driver)],

    states={
        DOING: [RegexHandler('^(Yes|No)$', doing)]
    },

    fallbacks=[CommandHandler('cancel', cancel)]
)
