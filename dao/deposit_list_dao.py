# -*- coding: utf-8 -*-
import logging
from util.common import log_stream_handler

# 将定义好的console日志handler添加到root logger
logging.getLogger(__name__).addHandler(log_stream_handler())
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


def select_by_teleId(teleId, page=0):
    logger.info("select_by_teleId %s %s", teleId, page)
    return dataBase.query(
        'select * from deposit_list where tele_id = %s order by create_time desc limit 10 offset %s',
        [teleId, int(page) * 10]
    )

#
# def update_status(**kwargs):
#     dataBase.execute(
#         'update order_info set order_status = %s where id = %s',
#         (kwargs['status'], kwargs['id']),
#         commit=True
#     )
