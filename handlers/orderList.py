# -*- coding: utf-8 -*-
import logging
from util.common import log_stream_handler

# 将定义好的console日志handler添加到root logger
logging.getLogger(__name__).addHandler(log_stream_handler())
logger = logging.getLogger(__name__)

from util.common import parse_cmd
from dao import order_info_dao


def handle(bot, update):
    logger.info("chatId: %s,first_name: %s,text: %s", update.message.chat_id, update.message.from_user.first_name,
                update.message.text)
    from_user = update.message.from_user
    cmd, text = parse_cmd(update.message.text)
    if text != None and text.isdigit():
        orders = order_info_dao.select_by_teleId(from_user.id, text)
    elif text == None:
        orders = order_info_dao.select_by_teleId(from_user.id)
    else:
        from util.common import order_list_notice_msg
        bot.send_message(chat_id=from_user.id,
                         text=order_list_notice_msg)
        return
    from util.common import order_title_msg
    from util.common import order_info_msg
    from util.common import order_status
    send_msg = "" + order_title_msg
    for order in orders:
        send_msg = send_msg + order_info_msg.format(order['id'],
                                                    order['item'],
                                                    order['price'],
                                                    order['create_time'],
                                                    order_status[order['order_status']])
    logger.info(send_msg.encode('utf-8'))
    bot.send_message(chat_id=update.message.from_user.id, text=send_msg)


command = 'orderList'

from telegram.ext import CommandHandler

handler = CommandHandler(command, handle)
