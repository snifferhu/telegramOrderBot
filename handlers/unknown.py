# -*- coding: utf-8 -*-
import logging

logger = logging.getLogger(__name__)


def handle(bot, update):
    logger.info("chatId: %s,first_name: %s,text: %s", update.message.chat_id, update.message.from_user.first_name,
                update.message.text)


command = 'unknown'

from telegram.ext import MessageHandler, Filters

handler = MessageHandler(Filters.command, handle)
