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
        'insert into driver_list (tele_id) values (%s)',
        (kwargs['tele_id'])
    )


def select_by_teleId(teleId):
    logger.info("select_by_teleId %s", teleId)
    return dataBase.query(
        'select * from driver_list where tele_id = %s', [teleId]
    )


def select_by_id(id):
    logger.info("select_by_id %s", id)
    return dataBase.query(
        'select * from driver_list where id = %s', [id]
    )


def update_status_by_teleId(open_status, teleId):
    logger.info("update_status_by_teleId %s %s", open_status, teleId)
    dataBase.execute(
        'update driver_list set open_status = %s where tele_id = %s', [open_status, teleId]
    )
