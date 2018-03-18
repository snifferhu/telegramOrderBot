# -*- coding: utf-8 -*-
import logging
from util.common import log_stream_handler

# 将定义好的console日志handler添加到root logger
logging.getLogger(__name__).addHandler(log_stream_handler())
logger = logging.getLogger(__name__)

from util.mysqlDB import DataBase
from util.core_config import db_config
from util.common import page_number
dataBase = DataBase(**db_config)


def insert(**kwargs):
    logger.info("insert %s", kwargs)
    dataBase.execute(
        'insert into order_info (id,member_id,nick_name,price,item,order_status) values (%s,%s,%s,%s,%s,%s)',
        (kwargs['order_id'], kwargs['tele_id'], kwargs['first_name'], kwargs['price'], kwargs['item'], '0')
    )


def select_by_teleId(teleId, page=1):
    logger.info("select_by_teleId %s", teleId)
    return dataBase.query(
        'select * from order_info where member_id = %s order by create_time desc limit %s offset %s',
        [teleId,page_number, (int(page) - 1) * page_number]
    )


def select_count_teleId(teleId):
    logger.info("select_by_teleId %s", teleId)
    return dataBase.query(
        'select count(*) from order_info where member_id = %s',
        [teleId]
    )[0]


def select_by_id(id):
    logger.info("select_by_id %s", id)
    return dataBase.query(
        'select * from order_info where id = %s', [id]
    )


def select_by_status(status, page=1):
    logger.info("select_by_status %s", status)
    return dataBase.query(
        'select * from order_info where order_status = %s order by create_time desc limit %s offset %s',
        [status,page_number, (int(page) - 1) * page_number]
    )


def select_count_status(status):
    logger.info("select_by_teleId %s", status)
    return dataBase.query(
        'select count(*) from order_info where order_status = %s',
        [status]
    )[0]


def update_status(**kwargs):
    logger.info("update_status %s", kwargs)
    return dataBase.execute(
        'update order_info set order_status = %s where id = %s',
        (kwargs['status'], kwargs['id'])
    )
