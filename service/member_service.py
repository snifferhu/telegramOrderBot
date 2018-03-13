# -*- coding: utf-8 -*-
import logging
from util.common import log_stream_handler
# 将定义好的console日志handler添加到root logger
logging.getLogger(__name__).addHandler(log_stream_handler())
logger = logging.getLogger(__name__)

from dao import deposit_list_dao
from dao import member_dao


def update_amount(tele_id, price, bef):
    logger.info("update_amount tele_id:%s, price:%s, bef:%s", tele_id, price, bef)
    deposit_list_dao.insert(tele_id=tele_id, price=price, bef=bef)
    member_dao.update_amout(tele_id=tele_id, price=price, bef=bef)
    member = member_dao.select_by_teleId(tele_id)
    logging.info(member)
    return member

def select_by_id(id):
    member = member_dao.select_by_id(id)
    logging.info(member)
    return member

def select_by_tele_id(tele_id):
    member = member_dao.select_by_teleId(tele_id)
    logging.info(member)
    return member