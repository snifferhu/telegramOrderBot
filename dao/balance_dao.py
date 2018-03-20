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
    logger.info(kwargs)
    dataBase.execute(
        'insert into balance_info (tele_id,nick_name,amount,driver_id,driver_tele_id) values (%s,%s,%s,%s,%s)',
        (kwargs['tele_id'], kwargs['nick_name'], 0.0, kwargs['driver_id'], kwargs['driver_tele_id'])
    )


def select_by_teleId(teleId, driver_tele_id):
    logger.info("select_by_teleId %s %s", teleId, driver_tele_id)
    return dataBase.query(
        'select * from balance_info where tele_id = %s and driver_tele_id = %s', [teleId, driver_tele_id]
    )


def select_all_by_teleId(teleId):
    logger.info("select_all_by_teleId %s", teleId)
    return dataBase.query(
        'select * from balance_info where tele_id = %s', [teleId]
    )


def select_by_id(id):
    logger.info("select_by_id %s", id)
    return dataBase.query(
        'select * from balance_info where id = %s', [id]
    )


def select_by_fee(driver_tele_id):
    logger.info("select_by_fee %s", 0)
    return dataBase.query(
        'select * from balance_info where amount < %s and driver_tele_id = %s', [0, driver_tele_id]
    )


def update_amount(price, tele_id, bef, driver_tele_id):
    logger.info("update_amount %s %s %s %s", price, tele_id, bef, driver_tele_id)
    dataBase.execute(
        'update balance_info set amount = amount + %s where tele_id = %s and amount = %s and driver_tele_id = %s',
        [price, tele_id, bef, driver_tele_id]
    )


def select_amount_by_member(tele_id, driver_id):
    logger.info("select_by_fee %s", 0)
    return dataBase.query(
        'select * from balance_info where tele_id = %s and driver_id = %s', [tele_id, driver_id]
    )
