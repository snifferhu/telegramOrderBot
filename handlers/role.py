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
    if update.message.chat_id != -1001385013271:
        return
        # 用户校验
    member = member_service.select_by_tele_id(from_user)
    member[0]["driver_id"] = "2"
    balance = balance_service.select_amount_by_member(member[0])
    if balance["amount"] < 1:
        update.message.reply_text("请到司机riley处充值，方可获得发言权")
        bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)
        return


command = 'role'

from telegram.ext import Filters, RegexHandler,MessageHandler

handler = MessageHandler( Filters.group, handle)
