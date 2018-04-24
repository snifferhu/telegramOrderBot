# -*- coding: utf-8 -*-
import logging
from util.common import log_stream_handler

# 将定义好的console日志handler添加到root logger
logging.getLogger(__name__).addHandler(log_stream_handler())
logger = logging.getLogger(__name__)

from util.mysqlDB import DataBase
from util.core_config import db_config

dataBase = DataBase(**db_config)


def select_by_id(id):
    logger.info("select_by_id %s", id)
    return dataBase.query(
        'select * from store_info where id = %s', [id]
    )
