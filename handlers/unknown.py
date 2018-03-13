# -*- coding: utf-8 -*-
import logging
from util.common import log_stream_handler
# 将定义好的console日志handler添加到root logger
logging.getLogger(__name__).addHandler(log_stream_handler())
logger = logging.getLogger(__name__)
from handlers.help import handle

# def handle(bot, update):
#     logger.info("chatId: %s,first_name: %s,text: %s", update.message.chat_id, update.message.from_user.first_name,
#                 update.message.text)


command = 'unknown'

from telegram.ext import MessageHandler, Filters

handler = MessageHandler(Filters.command, handle)
