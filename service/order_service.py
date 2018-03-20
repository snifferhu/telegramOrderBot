# -*- coding: utf-8 -*-
import logging
from util.common import log_stream_handler

# 将定义好的console日志handler添加到root logger
logging.getLogger(__name__).addHandler(log_stream_handler())
logger = logging.getLogger(__name__)

from dao import order_info_dao
from util.common import order_status
from util.common import order_title_msg
from util.common import ll_title_msg
from util.common import order_info_msg


def select_by_status(status, page=1, driver_id=1):
    logger.info("select_by_status %s %s %s", status, page, driver_id)
    orders = order_info_dao.select_by_status(status, page, driver_id)
    send_msg = "" + ll_title_msg
    for order in orders:
        send_msg = send_msg + order_info_msg.format(order['nick_name'],
                                                    order['id'],
                                                    order['item'],
                                                    int(order['price']),
                                                    order['create_time']
                                                    )
    return send_msg


def select_count_status(status, driver_id=1):
    return order_info_dao.select_count_status(status, driver_id)['count(*)']


def select_by_teleId(tele_id, page=1, driver_id=1):
    logger.info("select_by_teleId %s %s %s", tele_id, page, driver_id)
    orders = order_info_dao.select_by_teleId(tele_id, page)
    send_msg = "" + order_title_msg
    for order in orders:
        send_msg = send_msg + order_info_msg.format(order['id'],
                                                    order['item'],
                                                    int(order['price']),
                                                    order_status[order['order_status']],
                                                    order['create_time']
                                                    )
    return send_msg


def select_count_teleId(teleId):
    return order_info_dao.select_count_teleId(teleId)['count(*)']
