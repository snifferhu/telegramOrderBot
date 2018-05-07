# -*- coding: utf-8 -*-
import logging

from service import balance_service, member_service
from util.common import log_stream_handler

# 将定义好的console日志handler添加到root logger
logging.getLogger(__name__).addHandler(log_stream_handler())
logger = logging.getLogger(__name__)


def handle(bot, update):
    logger.info("chatId: %s,first_name: %s,text: %s",
                update.message.chat_id,
                update.message.from_user.first_name,
                update.message.text)
    from_user = update.message.from_user
        # 用户校验
    member = member_service.select_by_tele_id(from_user)
    if member[0]["driver_id"] == "-1":
        update.message.reply_text("雨季路滑请上车，方可获得发言权")
        bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)
        return
    member[0]["driver_id"] = "2"
    balance = balance_service.select_amount_by_member(member[0])
    if balance["amount"] < 0:
        # update.message.reply_text("请到司机处充值，方可获得发言权")
        bot.send_message(chat_id=from_user.id, text="请到司机处充值，方可获得发言权")
        bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)
        return


command = 'role'

from telegram.ext import Filters, MessageHandler

handler = MessageHandler((Filters.group & (~Filters.command)), handle)
