# -*- coding: utf-8 -*-
import logging
from util.common import log_stream_handler

# 将定义好的console日志handler添加到root logger
logging.getLogger(__name__).addHandler(log_stream_handler())
logger = logging.getLogger(__name__)

from util.common import balance_send_text
from dao import member_dao


def handle(bot, update):
    logger.info("chatId: %s,first_name: %s,text: %s", update.message.chat_id, update.message.from_user.first_name,
                update.message.text)
    from_user = update.message.from_user
    members = member_dao.select_by_cui()
    if len(members) == 0:
        bot.send_message(chat_id=from_user.id,
                         text='吹债结束')
    else:
        for member in members:
            bot.send_message(chat_id=from_user.id,
                     text=balance_send_text.format(member['nickName'],
                                                   member['amout'],
                                                   member['id']))
            bot.send_message(chat_id=member['tele_id'],
                     text=balance_send_text.format(member['nickName'],
                                                   member['amout'],
                                                   member['id']))


command = 'cui'

from telegram.ext import CommandHandler

handler = CommandHandler(command, handle)
