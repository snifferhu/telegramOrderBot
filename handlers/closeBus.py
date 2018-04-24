# -*- coding: utf-8 -*-
import logging
from util.common import log_stream_handler

# 将定义好的console日志handler添加到root logger
logging.getLogger(__name__).addHandler(log_stream_handler())
logger = logging.getLogger(__name__)

from util.common import driver_role_notice_text, driver_close_notice_text
from dao import driver_dao


def handle(bot, update):
    logger.info("chatId: %s,first_name: %s,text: %s", update.message.chat_id, update.message.from_user.first_name,
                update.message.text)
    from_user = update.message.from_user

    # 司机校验
    driver = driver_dao.select_by_teleId(from_user.id)
    if len(driver) == 0:
        update.message.reply_text(driver_role_notice_text)
        return

    driver_dao.update_status_by_teleId("1", from_user.id)
    bot.send_message(chat_id=from_user.id, text=driver_close_notice_text)


command = 'closeBus'

from telegram.ext import CommandHandler

handler = CommandHandler(command, handle)
