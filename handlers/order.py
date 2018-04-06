# -*- coding: utf-8 -*-
import logging, time

from service import balance_service, member_service
from util.common import log_stream_handler, order_balance_notice_msg

# 将定义好的console日志handler添加到root logger
logging.getLogger(__name__).addHandler(log_stream_handler())
logger = logging.getLogger(__name__)

from util.common import parse_cmd
from util.common import order_notice_msg
from util.common import order_detail_msg
from dao import order_info_dao, balance_dao
from dao import member_dao


def handle(bot, update):
    logger.info("chatId: %s,first_name: %s,text: %s",
                update.message.chat_id,
                update.message.from_user.first_name,
                update.message.text)
    from_user = update.message.from_user

    # 用户校验
    member = member_service.select_by_tele_id(from_user)

    cmd, text = parse_cmd(update.message.text)
    logger.info("%s  %s", cmd, text)
    order_info = update.message.text.replace("/order ", "").split("#")
    # 入参校验
    if text == None or len(text) == 0 or text.find('#') == -1 or (len(order_info) != 2):
        update.message.reply_text(order_notice_msg)
        return
    item, price = order_info
    item = item.strip()
    price = price.strip().replace("p", "").replace("P", "")

    if price.isdigit() == False:
        update.message.reply_text(order_notice_msg)
        return
    balance = balance_service.select_amount_by_member(member[0])
    if balance["amount"] < int(price):
        bot.send_message(chat_id=from_user.id, text=order_balance_notice_msg)
        send_text = balance_service.select_all_by_tele_id(member[0])
        bot.send_message(chat_id=from_user.id,
                         text=send_text)
        driver = member_service.select_driver(member[0])
        bot.send_message(chat_id=driver[0]['tele_id'],
                         text=send_text)
    #     return

    # 单号生成
    order_id = str(int(time.time()))[4:] + from_user.first_name[:1]
    logging.info("order id: %s", order_id)

    order_info_dao.insert(order_id=order_id,
                          tele_id=from_user.id,
                          first_name=member[0]['nickName'],
                          price=price,
                          item=item,
                          driver_id=member[0]['driver_id']
                          )

    bot.send_message(chat_id=from_user.id,
                     text=order_detail_msg.format(from_user.first_name,
                                                  item,
                                                  price,
                                                  order_id, member[0]['driver_id'])
                     )


command = 'order'

from telegram.ext import CommandHandler

handler = CommandHandler(command, handle)
