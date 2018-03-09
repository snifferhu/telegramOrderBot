# -*- coding: utf-8 -*-
import logging

logger = logging.getLogger(__name__)

from util.mysqlDB import DataBase
from util.core_config import db_config

dataBase = DataBase(**db_config)


def insert(**kwargs):
    logger.info("insert %s", kwargs)
    dataBase.execute(
        'insert into deposit_list (tele_id,price,bef,aft) values (%s,%s,%s,%s)',
        (kwargs['tele_id'], kwargs['price'], kwargs['bef'], float(kwargs['bef']) + float(kwargs['price']))
    )


def select_by_teleId(teleId):
    logger.info("select_by_teleId %s", teleId)
    return dataBase.query(
        'select * from deposit_list where tele_id = %s', [teleId]
    )

#
# def update_status(**kwargs):
#     dataBase.execute(
#         'update order_info set order_status = %s where id = %s',
#         (kwargs['status'], kwargs['id']),
#         commit=True
#     )
