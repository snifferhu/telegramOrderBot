# -*- coding: utf-8 -*-
import logging
from util.common import log_stream_handler
# 将定义好的console日志handler添加到root logger
logging.getLogger(__name__).addHandler(log_stream_handler())
logger = logging.getLogger(__name__)

from util.common import parse_cmd
from util.common import order_status
from dao import order_info_dao


def handle(bot, update):
    logger.info("chatId: %s,first_name: %s,text: %s", update.message.chat_id, update.message.from_user.first_name,
                update.message.text)
    cmd, text = parse_cmd(update.message.text)
    logger.info(order_status)
    logger.info(dir(order_status))
    if text == None:
        orders = order_info_dao.select_by_status("0")
    elif text.isdigit() == True and order_status.__contains__(text):
        orders = order_info_dao.select_by_status(text)
    else:
        bot.send_message(chat_id=update.message.chat_id, text="格式错误")
        return
    from util.common import order_title_msg
    from util.common import order_info_msg
    send_msg = "" + order_title_msg
    for order in orders:
        send_msg = send_msg + order_info_msg.format(order['id'],
                                                    order['item'],
                                                    order['price'],
                                                    order['create_time'],
                                                    order_status[order['order_status']])
    bot.send_message(chat_id=update.message.from_user.id, text=send_msg)


command = 'll'

from telegram.ext import CommandHandler

handler = CommandHandler(command, handle)
