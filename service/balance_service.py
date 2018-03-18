# -*- coding: utf-8 -*-
import logging
from util.common import log_stream_handler

# 将定义好的console日志handler添加到root logger
logging.getLogger(__name__).addHandler(log_stream_handler())
logger = logging.getLogger(__name__)

from dao import deposit_list_dao
from dao import member_dao, balance_dao, driver_dao
from util.common import balance_send_text, user_send_text, balance_all_send_text


def update_amount(tele_id, price, driver_tele_id):
    logger.info("update_amount tele_id:%s, price:%s, driver_tele_id:%s", tele_id, price, driver_tele_id)
    balance = balance_dao.select_by_teleId(tele_id, driver_tele_id)
    if len(balance) == 0:
        balance = insert_without_check(tele_id, driver_tele_id)
    deposit_list_dao.insert(tele_id=tele_id, price=price, bef=balance[0]["amount"])
    balance_dao.update_amount(tele_id=tele_id, price=price, bef=balance[0]["amount"], driver_tele_id=driver_tele_id)
    balance = balance_dao.select_by_teleId(tele_id, driver_tele_id)
    logging.info(balance)
    return balance[0]


def insert(tele_id, driver_tele_id):
    balance = balance_dao.select_by_teleId(tele_id, driver_tele_id)
    if len(balance) == 0:
        balance = insert_without_check(tele_id, driver_tele_id)
    logging.info(balance)
    return balance


def insert_without_check(tele_id, driver_tele_id):
    follow = member_dao.select_by_teleId(tele_id)
    driver = driver_dao.select_by_teleId(driver_tele_id)
    balance_dao.insert(tele_id=tele_id,
                       nick_name=follow[0]['nickName'],
                       driver_id=driver[0]['id'],
                       driver_tele_id=driver_tele_id)
    balance = balance_dao.select_by_teleId(tele_id, driver_tele_id)
    logging.info(balance)
    return balance


def select_by_tele_id(member, driver_tele_id):
    balance = balance_dao.select_by_teleId(member['tele_id'], driver_tele_id)
    logging.info(balance)
    return balance_send_text.format(
        balance[0]['nick_name'],
        balance[0]['amount'],
        member['id'],
        balance[0]['driver_id']
    )


def select_all_by_tele_id(member):
    balance_list = balance_dao.select_all_by_teleId(member['tele_id'])
    logging.info(balance_list)
    send_msg = user_send_text.format(member['nickName'], member['id'])
    for balance in balance_list:
        send_msg = send_msg + balance_all_send_text.format(
            balance['amount'],
            balance['driver_id']
        )
    return send_msg


def select_by_fee(driver_tele_id):
    balance_list = balance_dao.select_by_fee(driver_tele_id)
    send_msg_list = []
    for balance in balance_list:
        member = member_dao.select_by_teleId(balance['tele_id'])[0]
        balance_info = {
            "id": member['id'],
            "nick_name": member['nickName'],
            "tele_id": member['tele_id'],
            "amount": balance['amount'],
            "driver_id": balance['driver_id']
        }
        send_msg_list.append(balance_info)
    return send_msg_list
