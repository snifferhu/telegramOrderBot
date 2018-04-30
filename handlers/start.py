# -*- coding: utf-8 -*-
import logging
from util.common import log_stream_handler
# 将定义好的console日志handler添加到root logger
logging.getLogger(__name__).addHandler(log_stream_handler())
logger = logging.getLogger(__name__)

from util.common import start_send_text
from service import member_service


def handle(bot, update):
    logger.info("chatId: %s,first_name: %s,text: %s", update.message.chat_id, update.message.from_user.first_name,
                update.message.text)
    from_user = update.message.from_user
    # 用户校验
    member = member_service.select_by_tele_id(from_user)
    bot.send_message(chat_id=update.message.from_user.id, text=start_send_text)


command = 'start'

from telegram.ext import CommandHandler

handler = CommandHandler(command, handle)
