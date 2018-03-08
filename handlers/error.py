# -*- coding: utf-8 -*-
import logging
from telegram.error import *

logger = logging.getLogger(__name__)
from util.common import unauthorized_send_text


def handle(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)
    if isinstance(error, Unauthorized):
        update.message.reply_text(unauthorized_send_text)
        logger.warning('isinstance')
        return
    try:
        raise error
    except Unauthorized as u:
        update.message.reply_text(unauthorized_send_text)
        logger.warning('try raise except')


command = 'error'

from telegram.ext import CommandHandler

handler = CommandHandler(command, handle)
