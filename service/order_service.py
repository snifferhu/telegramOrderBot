# -*- coding: utf-8 -*-
import logging
from util.common import log_stream_handler

# 将定义好的console日志handler添加到root logger
logging.getLogger(__name__).addHandler(log_stream_handler())
logger = logging.getLogger(__name__)

from dao import order_info_dao
from util.common import order_status


def select_by_status(status, page=1):
    logger.info("select_by_status %s %s", status, page)
    orders = order_info_dao.select_by_status(status, page)
    from util.common import order_title_msg
    from util.common import order_info_msg
    send_msg = "" + order_title_msg
    for order in orders:
        send_msg = send_msg + order_info_msg.format(order['id'],
                                                    order['item'],
                                                    order['price'],
                                                    order['create_time'],
                                                    order_status[order['order_status']])
    return send_msg


def select_count_status(status):
    return order_info_dao.select_count_status(status)['count(*)']
