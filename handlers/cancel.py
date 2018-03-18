# -*- coding: utf-8 -*-
import logging
from util.common import log_stream_handler

# 将定义好的console日志handler添加到root logger
logging.getLogger(__name__).addHandler(log_stream_handler())
logger = logging.getLogger(__name__)

from util.common import parse_cmd
from util.common import cancel_notice_text
from util.common import null_notice_send_text
from util.common import status_note_msg
from util.common import order_title_msg
from util.common import order_info_msg
from util.common import order_status
from dao import order_info_dao, driver_dao
from service import member_service, balance_service


def handle(bot, update):
    logger.info("chatId: %s,first_name: %s,text: %s", update.message.chat_id, update.message.from_user.first_name,
                update.message.text)
    from_user = update.message.from_user
    cmd, text = parse_cmd(update.message.text)
    logger.info("%s  %s", cmd, text)
    if text == None or len(text) == 0:
        update.message.reply_text(cancel_notice_text)
        return
    send_msg = order_title_msg
    driver = driver_dao.select_by_teleId(from_user.id)
    tele_id = None
    for order_id in text.strip().split(' '):
        order = order_info_dao.select_by_id(order_id)
        logging.info("cancel orders:{0}".format(order))
        tele_id = order[0]['member_id']
        if len(order) == 0:
            bot.send_message(chat_id=from_user.id, text=null_notice_send_text.format(order_id))
            continue
        if order[0]['order_status'] == '1':
            bot.send_message(chat_id=from_user.id, text=status_note_msg.format(order_id))
            continue
        if order[0]['order_status'] == '0':
            order_info_dao.update_status(status='1', id=order_id)
        if order[0]['order_status'] == "2" and len(driver) == 1 and order[0]['driver_id'] == str(driver[0]['id']):
            balance_service.update_amount(order[0]['member_id'], order[0]['price'], from_user.id)
            bot.send_message(chat_id=from_user.id,
                             text='订单：{0}\n清退金额：{1}'.format(order[0]['id'], order[0]['price']))
            bot.send_message(chat_id=order[0]['member_id'],
                             text='订单：{0}\n清退金额：{1}'.format(order[0]['id'], order[0]['price']))

        if order[0]['order_status'] == "2" and (len(driver) == 0 or order[0]['driver_id'] != str(driver[0]['id'])):
            bot.send_message(chat_id=from_user.id, text='订单<{0}>状态为已接单，请联系司机处理'.format(order_id))

        order = order_info_dao.select_by_id(order_id)
        logging.info("cancel orders:{0}".format(order))
        send_msg = send_msg + order_info_msg.format(order[0]['id'],
                                                    order[0]['item'],
                                                    order[0]['price'],
                                                    order_status[order[0]['order_status']],
                                                    order[0]['create_time'])
    bot.send_message(chat_id=update.message.from_user.id, text=send_msg)
    if tele_id != None:
        bot.send_message(chat_id=tele_id, text=send_msg)


command = 'cancel'

from telegram.ext import CommandHandler

handler = CommandHandler(command, handle)
