# -*- coding: utf-8 -*-
import logging
from telegram.error import *
from util.common import log_stream_handler
from telegram import InlineKeyboardMarkup

# 将定义好的console日志handler添加到root logger
logging.getLogger(__name__).addHandler(log_stream_handler())
logger = logging.getLogger(__name__)
from util.common import unauthorized_send_text
from util.common import timeout_send_text


def handle(bot, update, error):
    """Log Errors caused by Updates."""
    try:
        logger.warning('Update "%s" caused error "%s"', update, error)
    except UnicodeEncodeError as uee:
        logger.warning('Update "%s" caused error "%s"', update, error.encode('utf-8'))
    if isinstance(error, Unauthorized):
        update.message.reply_text(unauthorized_send_text)
        logger.warning('Update "%s" caused error "%s"', update, error)
        return
    if isinstance(error, TimedOut):
        update.message.reply_text(timeout_send_text)
        logger.warning('Update time out %s"', error)
        return
    logger.warning('raise except %s', error)
    if update.message != None:
        update.message.reply_text('raise except {0}'.format(error))
    if update.callback_query != None:
        query = update.callback_query
        bot.edit_message_text(text='raise except {0}'.format(error),
                              chat_id=query.message.chat_id,
                              message_id=query.message.message_id,
                              reply_markup=InlineKeyboardMarkup([]))


command = 'error'

from telegram.ext import CommandHandler

handler = CommandHandler(command, handle)
