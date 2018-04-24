# -*- coding: utf-8 -*-
import logging, time

from service import member_service
from util.common import log_stream_handler

# 将定义好的console日志handler添加到root logger
logging.getLogger(__name__).addHandler(log_stream_handler())
logger = logging.getLogger(__name__)

from util.common import parse_cmd
from util.common import follow_notice_msg, follow_null_notice_msg, follow_send_msg
from dao import driver_dao
from dao import member_dao


def handle(bot, update):
    logger.info("chatId: %s,first_name: %s,text: %s",
                update.message.chat_id,
                update.message.from_user.first_name,
                update.message.text)
    from_user = update.message.from_user

    cmd, text = parse_cmd(update.message.text)
    logger.info("%s  %s", cmd, text)

    # 入参校验
    if text == None or len(text) == 0 or text.isdigit() == False:
        update.message.reply_text(follow_notice_msg)
        return

    driver = driver_dao.select_by_id(text)
    if (len(driver) == 0):
        update.message.reply_text(follow_null_notice_msg)
        return
    member = member_service.select_by_tele_id(from_user)
    if text != member[0]['driver_id']:
        member_dao.update_driver(from_user.id, text)
    driver_info = member_dao.select_by_teleId(driver[0]['tele_id'])

    bot.send_message(chat_id=from_user.id,
                     text=follow_send_msg.format(from_user.first_name,
                                                 member[0]['id'],
                                                 driver_info[0]['nickName'])
                     )
    # bot.send_message(chat_id=driver[0]['tele_id'],
    #                  text=follow_send_msg.format(from_user.first_name,
    #                                              driver_info[0]['nickName'])
    #                  )


command = 'follow'

from telegram.ext import CommandHandler

handler = CommandHandler(command, handle)
