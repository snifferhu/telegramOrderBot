# -*- coding: utf-8 -*-
import logging

logger = logging.getLogger(__name__)

from util.common import balance_send_text
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
        bot.send_message(chat_id=from_user.id,
                         text='输入参数，格式错误\n示例：/orderList [页码] \n示范：/orderList 1')
        return
    from util.common import order_title_mgs
    from util.common import order_info_mgs
    from util.common import order_status
    send_msg = "" + order_title_mgs
    for order in orders:
        send_msg = send_msg + order_info_mgs.format(order['id'],
                                                    order['item'],
                                                    order['price'],
                                                    order['create_time'],
                                                    order_status[order['order_status']])
    bot.send_message(chat_id=update.message.from_user.id, text=send_msg)


command = 'orderList'

from telegram.ext import CommandHandler

handler = CommandHandler(command, handle)
