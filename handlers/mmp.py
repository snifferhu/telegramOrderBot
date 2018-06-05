# -*- coding: utf-8 -*-
import logging
from util.common import log_stream_handler, deposit_send_text

# 将定义好的console日志handler添加到root logger
logging.getLogger(__name__).addHandler(log_stream_handler())
logger = logging.getLogger(__name__)

from util.common import parse_cmd
from service import member_service, balance_service
from util.common import deposit_notice_text, driver_role_notice_text
from dao import driver_dao

DOING, DONE = range(2)


def handle(bot, update):
    logger.info("chatId: %s,first_name: %s,text: %s", update.message.chat_id, update.message.from_user.first_name,
                update.message.text)
    from_user = update.message.from_user

    # 司机校验
    driver = driver_dao.select_by_teleId(from_user.id)
    if len(driver) == 0:
        update.message.reply_text(driver_role_notice_text)
        return
    cmd, text = parse_cmd(update.message.text)
    if text.find('#') == -1:
        update.message.reply_text()
        return

    id, price = text.split("#")
    member = member_service.select_by_id(id)
    logger.info("member:%s", member)
    if len(member) == 0:
        update.message.reply_text()
        return
    balance_service.update_amount(tele_id=member[0]["tele_id"],
                                  price=price,
                                  driver_tele_id=from_user.id)

    send_text = balance_service.select_by_tele_id(member[0], from_user.id)
    bot.send_message(chat_id=from_user.id,
                     text=send_text)
    send_text = deposit_send_text.format(from_user.first_name, price) + send_text

    bot.send_message(chat_id=member[0]['tele_id'],
                     text=send_text)


command = 'mmp'

from telegram.ext import CommandHandler

handler = CommandHandler(command, handle)
