# -*- coding: utf-8 -*-
import logging, time

from service import balance_service
from util.common import log_stream_handler, driver_role_notice_text, order_over_notice_msg, order_title_msg, \
    order_info_msg, order_status, over_title_msg, over_info_msg

# 将定义好的console日志handler添加到root logger
logging.getLogger(__name__).addHandler(log_stream_handler())
logger = logging.getLogger(__name__)

from util.common import parse_cmd
from util.common import order_notice_msg
from util.common import order_detail_msg
from dao import order_info_dao, driver_dao
from random import randint


def handle(bot, update):
    logger.info("chatId: %s,first_name: %s,text: %s",
                update.message.chat_id,
                update.message.from_user.first_name,
                update.message.text)
    from_user = update.message.from_user
    cmd, text = parse_cmd(update.message.text)

    # 司机校验
    driver = driver_dao.select_by_teleId(from_user.id)
    if len(driver) == 0:
        update.message.reply_text(driver_role_notice_text)
        return

    order_list = order_info_dao.select_init_driver_id(driver[0]['id'])
    if len(order_list) == 0:
        update.message.reply_text(order_over_notice_msg)
        return

    send_msg_list = []
    for order in order_list:
        logger.info("over order id:%s,nick_name:%s,price:%s,driver_id:%s",
                    order["id"], order["nick_name"],
                    order["price"], order["driver_id"])
        balance = balance_service.update_amount(order["member_id"], -order["price"], from_user.id)
        status = "3" if balance["amount"] > 0 else "2"
        order_info_dao.update_status(status=status, id=order["id"])
        send_msg_list.append({
            "id": balance["id"],
            "amount": balance["amount"],
            "order_id": order["id"],
            "tele_id": order["member_id"],
            "nick_name": order["nick_name"],
            "price": order["price"],
            "create_time": order["create_time"],
            "item": order["item"],
            "status": status
        })

    send_msg = over_title_msg
    total_price = 0
    for send_msg_info in send_msg_list:
        send_order_msg = over_info_msg.format(
            send_msg_info["nick_name"],
            send_msg_info["item"],
            send_msg_info["price"]
        )
        send_msg = send_msg + send_order_msg
        bot.send_message(chat_id=send_msg_info["tele_id"],
                         text=over_title_msg + send_order_msg + "\n余额：{0}".format(send_msg_info["amount"]))

        total_price = total_price + int(send_msg_info["price"])
    number = int(text) if text != None and text.isdigit() else int(len(order_list) / 10) - 1
    for tmp in range(number):
        random_order = random_send_msg(send_msg_list, from_user)
        bot.send_message(chat_id=update.message.chat_id, text="请 <{0}> 协助拿饭".format(random_order["nick_name"]))
        bot.send_message(chat_id=random_order["tele_id"], text="请 <{0}> 协助拿饭".format(random_order["nick_name"]))
    send_msg = send_msg + "\n合计：{0} \t份数：{1}".format(total_price, len(order_list))
    bot.send_message(chat_id=update.message.chat_id, text=send_msg)


command = 'over'


def random_send_msg(send_msg_list, from_user, time=3):
    random_order = send_msg_list[randint(0, len(send_msg_list) - 1)]
    if random_order["tele_id"] == from_user.id and time > 0:
        return random_send_msg(send_msg_list, from_user, --time)
    else:
        return random_order


from telegram.ext import CommandHandler

handler = CommandHandler(command, handle)
