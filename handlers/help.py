# -*- coding: utf-8 -*-
import logging
from util.common import log_stream_handler
# 将定义好的console日志handler添加到root logger
logging.getLogger(__name__).addHandler(log_stream_handler())
logger = logging.getLogger(__name__)

from util.common import help_send_text
from util.common import help_send_text_1
from util.common import help_send_text_2
from util.common import help_send_text_3


def handle(bot, update):
    logger.info("chatId: %s,first_name: %s,text: %s", update.message.chat_id, update.message.from_user.first_name,
                update.message.text)
    bot.send_message(chat_id=update.message.from_user.id, text=help_send_text)
    # bot.send_message(chat_id=update.message.from_user.id, text=help_send_text_1)
    # bot.send_message(chat_id=update.message.from_user.id, text=help_send_text_2)
    # bot.send_message(chat_id=update.message.from_user.id, text=help_send_text_3)


command = 'help'

from telegram.ext import CommandHandler

handler = CommandHandler(command, handle)