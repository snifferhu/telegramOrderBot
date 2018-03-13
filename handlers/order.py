# -*- coding: utf-8 -*-
import logging, time

logger = logging.getLogger(__name__)

from util.common import parse_cmd
from util.common import order_notice_msg
from util.common import order_detail_msg
from dao import order_info_dao
from dao import member_dao


def handle(bot, update):
    logger.info("chatId: %s,first_name: %s,text: %s",
                update.message.chat_id,
                update.message.from_user.first_name,
                update.message.text)
    from_user = update.message.from_user

    # 用户校验
    member = member_dao.select_by_teleId(from_user.id)
    if len(member) == 0:
        member_dao.insert(username=from_user.username,
                          first_name=from_user.first_name,
                          tele_id=from_user.id)

    cmd, text = parse_cmd(update.message.text)
    logger.info("%s  %s", cmd, text)

    # 入参校验
    if text == None or len(text) == 0 or text.find('#') == -1:
        update.message.reply_text(order_notice_msg)
        return
    order_info = update.message.text.replace("/order ", "").split("#")
    if (len(order_info) != 2) or (order_info[1].isdigit() == False):
        update.message.reply_text(order_notice_msg)
        return

    # 单号生成
    order_id = str(int(time.time()))[4:] + from_user.first_name[:1]
    logging.info("order id: %s", order_id)

    order_info_dao.insert(order_id=order_id,
                          tele_id=from_user.id,
                          first_name=member[0]['nickName'],
                          price=order_info[1],
                          item=order_info[0])

    bot.send_message(chat_id=from_user.id,
                     text=order_detail_msg.format(from_user.first_name, order_info[0], order_info[1], order_id))


command = 'order'

from telegram.ext import CommandHandler

handler = CommandHandler(command, handle)
