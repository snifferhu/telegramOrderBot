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
        'insert into member (name,nickName,amout,phone,tele_id) values (%s,%s,%s,%s,%s)',
        (kwargs['username'], kwargs['first_name'], 0.0, '', kwargs['tele_id'])
    )


def select_by_teleId(teleId):
    logger.info("select_by_teleId %s", teleId)
    return dataBase.query(
        'select * from member where tele_id = %s', [teleId]
    )


def select_by_id(id):
    logger.info("select_by_id %s", id)
    return dataBase.query(
        'select * from member where id = %s', [id]
    )


def select_by_cui():
    logger.info("select_by_cui %s", 0)
    return dataBase.query(
        'select * from member where amout < %s', [0]
    )

def update_amout(price, tele_id, bef):
    logger.info("update_amout %s %s %s", price, tele_id, bef)
    dataBase.execute(
        'update member set amout = amout + %s where tele_id = %s and amout = %s',
        [price, tele_id, bef]
    )
