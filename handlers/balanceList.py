# -*- coding: utf-8 -*-
import logging
from util.common import log_stream_handler

# 将定义好的console日志handler添加到root logger
logging.getLogger(__name__).addHandler(log_stream_handler())
logger = logging.getLogger(__name__)

from util.common import parse_cmd
from dao import deposit_list_dao


def handle(bot, update):
    logger.info("chatId: %s,first_name: %s,text: %s", update.message.chat_id, update.message.from_user.first_name,
                update.message.text)
    from_user = update.message.from_user
    cmd, text = parse_cmd(update.message.text)
    if text != None and text.isdigit():
        balance_list = deposit_list_dao.select_by_teleId(from_user.id, text)
    elif text == None:
        balance_list = deposit_list_dao.select_by_teleId(from_user.id)
    else:
        from util.common import balance_list_notice_msg
        bot.send_message(chat_id=from_user.id,
                         text=balance_list_notice_msg)
        return
    from util.common import bal_title_msg
    from util.common import bal_info_msg
    send_msg = "" + bal_title_msg
    for balance in balance_list:
        send_msg = send_msg + bal_info_msg.format(int(balance['price']),
                                                  int(balance['bef']),
                                                  int(balance['aft']),
                                                  balance['create_time'])
    logger.info(send_msg)
    bot.send_message(chat_id=update.message.from_user.id, text=send_msg)


command = 'balanceList'

from telegram.ext import CommandHandler

handler = CommandHandler(command, handle)
