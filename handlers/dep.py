# -*- coding: utf-8 -*-
import logging
from util.common import log_stream_handler

# 将定义好的console日志handler添加到root logger
logging.getLogger(__name__).addHandler(log_stream_handler())
logger = logging.getLogger(__name__)

from handlers.deposit import deposit, doing, cancelDeposit, DOING

command = 'dep'

from telegram.ext import ConversationHandler, CommandHandler, Filters, MessageHandler

handler = ConversationHandler(
    entry_points=[CommandHandler(command, deposit)],

    states={
        DOING: [MessageHandler(Filters.text, doing)]
    },

    fallbacks=[CommandHandler('cancelDeposit', cancelDeposit)]
)
