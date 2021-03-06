# -*- coding: utf-8 -*-
import logging

logger = logging.getLogger(__name__)


def parse_cmd(text):
    # Telegram understands UTF-8, so encode text for unicode compatibility
    # text = text.encode('utf-8')
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

timeout_send_text = '''
请求超时，请稍后！
'''

user_send_text = '''大佬：<{0}>
编号：{1}'''

balance_send_text = '''
司机车牌：{3}

大佬：<{0}>
余额：{1}
编号：{2}
'''

balance_all_send_text = '''
司机车牌：{1}
余额：{0}'''

cancel_notice_text = '''
格式错误
示例：/cancel [单号] [单号] 
示范：/cancel 1519106642s 1519106643s
'''

null_notice_send_text = '''
单号<{0}>，不存在
'''

status_note_msg = '''
单号<{0}>，已删除
'''

bal_title_msg = '''
金额\t前\t后\t时间
'''
bal_info_msg = '''
{0}\t{1}\t{2}\t{3}'''

dl_title_msg = '''
时间\t金额\t前\t后\t编号\t户名
'''
dl_info_msg = '''
{5}\t\t{2}\t\t{3}\t\t{4}\t\t\t\t\t\t\t\t\t\t\t\t\t\t<{0}>\t\t{1}'''

fl_title_msg = '''
编号\t户名\t金额
'''

fl_info_msg = '''
{0}\t\t\t{1}\t\t\t{2}'''

order_title_msg = '''
编号\t详情\t金额\t状态\t下单时间'''

ll_title_msg = '''
下单时间\t编号\t金额\t详情\t户名'''

order_info_msg = '''
{4}\t\t\t\t\t\t\t\t\t\t\t\t<{1}>\t{3}\t[{2}]\t\t\t\t\t{0}'''

over_title_msg = '''
户名\t详情\t金额'''

over_info_msg = '''
{0}\t<{1}>\t{2}'''

search_title_msg = '''
编号\t户名\t'''

search_info_msg = '''
<{0}>\t{1}'''

order_detail_msg = '''
大佬，<{0}>
订单为：{1}
金额为：{2}
订单号：{3}
车牌号：{4}
'''

order_notice_msg = '''格式错误
示例：/order [订单信息]#[金额] 
示范：/order A1 B1 C1#160'''

order_fail_notice_msg = '''
下单失败，已欠费，尽快缴费！'''

order_balance_notice_msg = '''
下单已成功，但是余额不足，尽快缴费！'''

order_over_notice_msg = '''
尚无订单'''

role_send_text = '''
此功能仅限管理员使用，如有疑问请及时联系管理员
'''

member_cnt_find_text = '''
相应用户不存在。
'''

deposit_notice_text = '''
/cancelDeposit or [no]#[price]
'''

deposit_send_text = '''
司机：<{0}>
为您充值：{1}
'''

balance_list_notice_msg = '''
输入参数，格式错误
示例：/balanceList \tor /bl
示范：/balanceList \t/bl 
'''

order_list_notice_msg = '''
输入参数，格式错误
示例：/orderList\tor /ol
示范：/orderList tor /ol 
'''

help_send_text = '''
----------入 门 须 知-----------
新手上车需找到机器人激活：
/start - 回复你：“start！来跟我念，诗达儿特。”
自此创建账户

/help - 帮助信息

----------订单相关命令----------
/follow - 跟车命令，默认跟车1号(sniff车)，所有订单命令将会以跟车号维系
/f - 跟车命令，默认跟车1号(sniff车)，所有订单命令将会以跟车号维系
/menu - 对应车牌下，菜单信息
/order - 下单命令
/cancel - 撤销订单，默认撤销最后一份订单
/orderList  - 查看本人历史订单记录
/ol - 查看本人历史订单记录

----------余额相关命令----------
/balance - 查看本人钱包余额
/bal - 查看本人钱包余额
/balanceList - 查看本人钱包充值记录
/bl - 查看本人钱包充值记录
/depositList - 查看所有钱包充值记录
/dl - 查看所有钱包充值记录

----------管理相关命令----------
/driver - 申请开车命令，申请开车请参与培训、考取驾照
/ll - 查看本趟列车上，所有乘客订单信息
/over - 截单命令，进入收账周期
/feeList - 乘客列表命令，分别根据id、name、money排序
/fl - 乘客列表命令，分别根据id、name、money排序
/fee - 催单命令，截单后私聊催促欠费乘客
/openBus - 开始点餐啦！
/closeBus - 停止点餐啦！
'''

driver_close_msg = '''
<{}>号司机，猛踩刹车
乘客请注意抓好扶手，下车请注意先下后上
'''

order_status = {"0": "init", "1": "cancel", "2": "over", "3": "received"}


def log_stream_handler():
    # 定义一个Handler打印INFO及以上级别的日志到sys.stderr
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    # 设置日志打印格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console.setFormatter(formatter)
    return console


driver_start_text = '''
大佬<{0}>，可欲开车？
'''

driver_role_notice_text = '''
此功能仅为司机开放，如欲加入司机团队。
请 /driver
'''

driver_open_notice_text = '''
开始点餐啦！
'''

driver_close_notice_text = '''
停止点餐啦！
'''
driver_yes_msg = '''
司机 <{0}>
您的车牌号为：{1}
'''

follow_notice_msg = '''
输入参数，格式错误
示例：/follow [车牌号]
示范：/follow 1
'''

follow_null_notice_msg = '''
您所提供的车牌号，没找到对应的司机
'''

follow_send_msg = '''
滴滴滴，学生卡 -> {0}
编号 -> {1}
成功上 -> {2} 车
'''

page_number = 30
