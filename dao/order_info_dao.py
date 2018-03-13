# -*- coding: utf-8 -*-
import logging

logger = logging.getLogger(__name__)

from util.mysqlDB import DataBase
from util.core_config import db_config

dataBase = DataBase(**db_config)


def insert(**kwargs):
    logger.info("insert %s", kwargs)
    dataBase.execute(
        'insert into order_info (id,member_id,nick_name,price,item,order_status) values (%s,%s,%s,%s,%s,%s)',
        (kwargs['order_id'], kwargs['tele_id'], kwargs['first_name'], kwargs['price'], kwargs['item'], '0')
    )


def select_by_teleId(teleId, page=0):
    logger.info("select_by_teleId %s", teleId)
    return dataBase.query(
        'select * from order_info where member_id = %s order by create_time desc limit 10 offset %s', [teleId, int(page) * 10]
    )


def select_by_id(id):
    logger.info("select_by_id %s", id)
    return dataBase.query(
        'select * from order_info where id = %s', [id]
    )


def select_by_status(status):
    logger.info("select_by_status %s", status)
    return dataBase.query(
        'select * from order_info where order_status = %s order by nick_name', [status]
    )


def update_status(**kwargs):
    logger.info("update_status %s", kwargs)
    return dataBase.execute(
        'update order_info set order_status = %s where id = %s',
        (kwargs['status'], kwargs['id'])
    )
