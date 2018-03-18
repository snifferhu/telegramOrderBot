# -*- coding: utf-8 -*-
import logging

from service import balance_service
from util.common import log_stream_handler

# 将定义好的console日志handler添加到root logger
logging.getLogger(__name__).addHandler(log_stream_handler())
logger = logging.getLogger(__name__)

from util.common import balance_send_text
from util.common import driver_role_notice_text
from dao import member_dao


def handle(bot, update):
    logger.info("chatId: %s,first_name: %s,text: %s", update.message.chat_id, update.message.from_user.first_name,
                update.message.text)
    from_user = update.message.from_user
    user = member_dao.select_by_teleId(from_user.id)
    if user[0]["is_driver"] == 1:
        balance_list = balance_service.select_by_fee(from_user.id)
        if len(balance_list) == 0:
            bot.send_message(chat_id=from_user.id,
                             text='吹债结束')
        else:
            for balance_info in balance_list:
                bot.send_message(chat_id=balance_info['tele_id'],
                                 text=balance_send_text.format(balance_info['nick_name'],
                                                               balance_info['amount'],
                                                               balance_info['id'],
                                                               balance_info['driver_id']
                                                               )
                                 )
                bot.send_message(chat_id=from_user.id,
                                 text=balance_send_text.format(balance_info['nick_name'],
                                                               balance_info['amount'],
                                                               balance_info['id'],
                                                               balance_info['driver_id']
                                                               )
                                 )

    else:
        bot.send_message(chat_id=update.message.chat_id, text=driver_role_notice_text)


command = 'fee'

from telegram.ext import CommandHandler

handler = CommandHandler(command, handle)
