# -*- coding: utf-8 -*-
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
# 将定义好的console日志handler添加到root logger
import logging
from util.common import log_stream_handler
from util.common import page_number
logging.getLogger(__name__).addHandler(log_stream_handler())
logger = logging.getLogger(__name__)


def create_button(view, data):
    logger.info("create_button(view=%s, data=%s)", view, data)
    return InlineKeyboardButton(view, callback_data=data)


def create_pre_button(prefix, page_index, status):
    logger.info("create_pre_button(prefix=%s, page_index=%s, status=%s)", prefix, page_index, status)
    return InlineKeyboardButton("pre", callback_data="{0}_pre_{1}_{2}".format(prefix, (page_index) - 1, status))


def create_next_button(prefix, page_index, status):
    logger.info("create_next_button(prefix=%s, page_index=%s, status=%s)", prefix, page_index, status)
    return InlineKeyboardButton("next", callback_data="{0}_next_{1}_{2}".format(prefix, (page_index) + 1, status))


def create_close_button(prefix):
    return [InlineKeyboardButton("over", callback_data="{0}_close".format(prefix))]


def create_page_button_list(count, prefix, pageIndex=1, status="0"):
    logger.info("create_page_button_list(count=%s, prefix=%s, pageIndex=%s, status=%s)",
                count,
                prefix,
                pageIndex,
                status)
    if pageIndex == 1:
        button_list = []
    else:
        button_list = [create_pre_button(prefix, pageIndex, status)]
    page_count = int(count / page_number) + 1 if count % page_number > 0 else 0
    tmp_page_flag = pageIndex + 3 if pageIndex + 3 <= page_count else page_count
    logger.info("create_page_button_list page_count %s,tmp_page_flag %s", page_count, tmp_page_flag)
    for page in range(tmp_page_flag - 3, tmp_page_flag + 1):
        data = "{0}_page_{1}_{2}".format(prefix, page, status)
        if page == pageIndex:
            page = "[ {0} ]".format(page)
        button_list.append(create_button(page, data))
    if page_count != pageIndex:
        button_list.append(create_next_button(prefix, pageIndex, status))
    return button_list

def default():
    return '参数有误，请及时联系管理员.', []


def close():
    return '再见! 期待下一次的合作.', []