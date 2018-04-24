# -*- coding: utf-8 -*-
import logging
from util.common import log_stream_handler, bal_title_msg, bal_info_msg, fl_title_msg, fl_info_msg

# 将定义好的console日志handler添加到root logger
logging.getLogger(__name__).addHandler(log_stream_handler())
logger = logging.getLogger(__name__)

from dao import driver_dao, store_dao
from service import member_service


def select_by_from_user(from_user):
    logger.info("select_by_from_user %s", from_user)
    member = member_service.select_by_tele_id(from_user)

    driver = driver_dao.select_by_id(member[0]['driver_id'])

    return store_dao.select_by_id(driver[0]['store_id'])
