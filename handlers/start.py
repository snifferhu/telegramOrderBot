# -*- coding: utf-8 -*-
import logging

logger = logging.getLogger(__name__)

from util.common import start_send_text


def handle(bot, update):
    logger.info("chatId: %s,first_name: %s,text: %s", update.message.chat_id, update.message.from_user.first_name,
                update.message.text)
    bot.send_message(chat_id=update.message.from_user.id, text=start_send_text)


command = 'start'

from telegram.ext import CommandHandler

handler = CommandHandler(command, handle)
