# -*- coding: utf-8 -*-
import logging
from util.common import log_stream_handler

# 将定义好的console日志handler添加到root logger
logging.getLogger(__name__).addHandler(log_stream_handler())
logger = logging.getLogger(__name__)

from util.common import help_send_text, parse_cmd, search_title_msg, search_info_msg
from dao import member_dao
from service import balance_service


def handle(bot, update):
    logger.info("chatId: %s,first_name: %s,text: %s", update.message.chat_id, update.message.from_user.first_name,
                update.message.text)
    from_user = update.message.from_user
    cmd, text = parse_cmd(update.message.text)
    if text == None:
        bot.send_message(chat_id=update.message.from_user.id, text=help_send_text)
    members = member_dao.select_by_nickName(text.strip())
    send_text = search_title_msg
    for member in members:
        send_text = send_text + search_info_msg.format(member['id'], member['nickName'])
        send_text = send_text + balance_service.select_all_by_tele_id(member)
    bot.send_message(chat_id=update.message.from_user.id, text=send_text)


command = 'search'

from telegram.ext import CommandHandler

handler = CommandHandler(command, handle)
