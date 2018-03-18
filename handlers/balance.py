# -*- coding: utf-8 -*-
import logging

from service import balance_service
from util.common import log_stream_handler

# 将定义好的console日志handler添加到root logger
logging.getLogger(__name__).addHandler(log_stream_handler())
logger = logging.getLogger(__name__)

from dao import member_dao


def handle(bot, update):
    logger.info("chatId: %s,first_name: %s,text: %s", update.message.chat_id, update.message.from_user.first_name,
                update.message.text)
    from_user = update.message.from_user
    member = member_dao.select_by_teleId(from_user.id)
    if len(member) == 0:
        member_dao.insert(username=from_user.username,
                          first_name=from_user.first_name,
                          tele_id=from_user.id)
        member = member_dao.select_by_teleId(from_user.id)
    send_text = balance_service.select_all_by_tele_id(member[0])
    bot.send_message(chat_id=from_user.id,
                     text=send_text)


command = 'balance'

from telegram.ext import CommandHandler

handler = CommandHandler(command, handle)
