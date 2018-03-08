# -*- coding: utf-8 -*-
import logging

logger = logging.getLogger(__name__)


def parse_cmd(text):
    # Telegram understands UTF-8, so encode text for unicode compatibility
    text = text.encode('utf-8')
    cmd = None
    if '/' in text:
        try:
            index = text.index(' ')
        except ValueError as e:
            return (text, None)
        cmd = text[:index]
        text = text[index + 1:]
    # if cmd != None and '@' in cmd:
    #     cmd = cmd.replace(bot_name, '')
    logger.info("cmd:{0},text:{1}".format(cmd, text))
    return (cmd, text)


NOTE_PUBLIC_TEXT = '''
谨防信息泄漏，仅限私聊使用
'''

start_send_text = '''start！来跟我念，诗达儿特。'''

unauthorized_send_text = '''
如果出现此文字，说明您尚未激活机器人
请私聊此机器人，点击start按钮激活机器人服务
'''

balance_send_text = '''
大佬：<{0}>
余额：{1}
编号：{2}
'''

role_send_text = '''
此功能仅限管理员使用，如有疑问请及时联系管理员
'''

member_cnt_find_text = '''
相应用户不存在。
'''

deposit_notice_text = '''
/cancel or [no]#[price]
'''

help_send_text = '''
/help - 帮助信息

----------订单相关命令----------
/follow - 跟车命令，默认跟车1号(sniff车)，所有订单命令将会以跟车号维系
/menu - 对应车牌下，菜单信息
/order - 下单命令
/ol - 查看本人历史订单记录；参数数值为页数，-1为查所有，每页10条；默认查询第一页
/cancel - 申请撤销订单，需与列车长确认订单状态

----------余额相关命令----------
/bal - 查看本人钱包余额
/bl - 查看本人钱包充值记录；参数数值为页数，-1为查所有，每页10条；默认查询第一页

----------管理相关命令----------
/driver - 申请开车命令，选择餐馆、确认餐馆信息、维护餐馆信息、获得车牌号
/ll - 查看本趟列车上，所有乘客订单信息
    查询参数："0": "init", "1": "cancel", "2": "over", "3": "received"
    默认查询 init
/over - 截单命令，进入收账周期
/rece - receive收账命令
'''

help_send_text_1 = '''
/help - 帮助信息

----------订单相关命令----------
/follow - 跟车命令，默认跟车1号(sniff车)，所有订单命令将会以跟车号维系
/menu - 对应车牌下，菜单信息
/order - 下单命令
/ol - 查看本人历史订单记录；参数数值为页数，-1为查所有，每页10条；默认查询第一页
/cancel - 申请撤销订单，需与列车长确认订单状态
'''

help_send_text_2 = '''
----------余额相关命令----------
/bal - 查看本人钱包余额
/bl - 查看本人钱包充值记录；参数数值为页数，-1为查所有，每页10条；默认查询第一页
'''

help_send_text_3 = '''
----------管理相关命令----------
/driver - 申请开车命令，选择餐馆、确认餐馆信息、维护餐馆信息、获得车牌号
/ll - 查看本趟列车上，所有乘客订单信息
    查询参数：init: 0, cancel: 1, over: 2, received: 3
/over - 截单命令，进入收账周期
/rece - receive收账命令
'''

status = {"0": "init", "1": "cancel", "2": "over", "3": "received"}