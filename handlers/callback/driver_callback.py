# -*- coding: utf-8 -*-
import logging
from util.common import log_stream_handler

# 将定义好的console日志handler添加到root logger
logging.getLogger(__name__).addHandler(log_stream_handler())
logger = logging.getLogger(__name__)

from telegram import InlineKeyboardButton
from dao import driver_dao, member_dao
from util.telegram_bot_util import default
from util.common import driver_yes_msg

prefix = 'dr'

close_button = [InlineKeyboardButton("close", callback_data='bl_close')]


def exec(query_params):
    logger.info(query_params)
    if query_params[1] == "Yes":
        tele_id = query_params[2]
        return yes(tele_id)
    elif query_params[1] == "No":
        return no()
    else:
        return default()


def yes(tele_id):
    driver = driver_dao.select_by_teleId(tele_id)
    if len(driver) == 0:
        driver_dao.insert(tele_id=tele_id)
        driver = driver_dao.select_by_teleId(tele_id)
    user = member_dao.select_by_teleId(tele_id)
    send_msg = driver_yes_msg.format(user[0]['nickName'], driver[0]['id'])
    return send_msg, []


def no():
    return '再见! 期待下一次的合作.', []
