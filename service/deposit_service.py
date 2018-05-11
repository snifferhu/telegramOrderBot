# -*- coding: utf-8 -*-
import logging
from util.common import log_stream_handler

# 将定义好的console日志handler添加到root logger
logging.getLogger(__name__).addHandler(log_stream_handler())
logger = logging.getLogger(__name__)

from dao import deposit_list_dao
from util.common import bal_title_msg, dl_title_msg
from util.common import bal_info_msg, dl_info_msg


def select_by_teleId(tele_id, page=1):
    logger.info("select_by_teleId %s %s", tele_id, page)
    balance_list = deposit_list_dao.select_by_teleId(tele_id, page)
    send_msg = "" + bal_title_msg
    for balance in balance_list:
        send_msg = send_msg + bal_info_msg.format(int(balance['price']),
                                                  int(balance['bef']),
                                                  int(balance['aft']),
                                                  balance['create_time'])
    return send_msg


def select_count_teleId(teleId):
    return deposit_list_dao.select_count_teleId(teleId)['count(*)']


def select_by_driverId(current_page):
    logger.info("select_by_driverId  %s", current_page)
    balance_list = deposit_list_dao.select_by_all(current_page)
    send_msg = "" + dl_title_msg
    for balance in balance_list:
        send_msg = send_msg + dl_info_msg.format(balance['id'],
                                                 balance['nickName'],
                                                 int(balance['price']),
                                                 int(balance['bef']),
                                                 int(balance['aft']),
                                                 balance['create_time'])
    return send_msg


def select_count_driverId():
    return deposit_list_dao.select_count_all()['count(*)']
