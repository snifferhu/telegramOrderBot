# -*- coding: utf-8 -*-
import logging
from util.common import log_stream_handler
# 将定义好的console日志handler添加到root logger
logging.getLogger(__name__).addHandler(log_stream_handler())
logger = logging.getLogger(__name__)

from handlers.orderList import handle

command = 'ol'

from telegram.ext import CommandHandler

handler = CommandHandler(command, handle)
