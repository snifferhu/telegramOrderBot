# -*- coding: utf-8 -*-
import logging

logger = logging.getLogger(__name__)

from util.common import balance_send_text
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
    bot.send_message(chat_id=from_user.id,
                     text=balance_send_text.format(member[0]['nickName'].encode("utf-8"),
                                                   member[0]['amout'],
                                                   member[0]['id']))


command = 'balance'

from telegram.ext import CommandHandler

handler = CommandHandler(command, handle)
