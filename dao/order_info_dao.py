# -*- coding: utf-8 -*-
import logging

logger = logging.getLogger(__name__)

from lib.mysqlPool import MySQLPool
from lib.core_config import db_config

dataBase = MySQLPool(**db_config)


def insert(**kwargs):
    logger.info("insert %s",kwargs)
    dataBase.execute(
        'insert into order_info (id,member_id,nick_name,price,item,order_status) values (%s,%s,%s,%s,%s,%s)',
        (kwargs['order_id'],   kwargs['tele_id'],   kwargs['first_name'],   kwargs['price'], kwargs['first_name'],  '0'),
        commit=True
    )

def select_by_teleId(teleId):
    logger.info("select_by_teleId %s",teleId)
    return dataBase.execute(
        'select * from order_info where tele_id = %s', [teleId]
    )

def select_by_status(status):
    logger.info("select_by_status %s", status)
    return dataBase.execute(
        'select * from order_info where order_status = %s', [status]
    )

def update_status(**kwargs):
    logger.info("update_status %s", kwargs)
    dataBase.execute(
        'update order_info set order_status = %s where id = %s',
        (kwargs['status'], kwargs['id']),
        commit=True
    )
