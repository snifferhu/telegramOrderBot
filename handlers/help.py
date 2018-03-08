# -*- coding: utf-8 -*-
import logging

logger = logging.getLogger(__name__)

from lib.common import help_send_text
from lib.common import help_send_text_1
from lib.common import help_send_text_2
from lib.common import help_send_text_3


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