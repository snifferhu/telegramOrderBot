# -*- coding: utf-8 -*-
import logging

logger = logging.getLogger(__name__)

from handlers.orderList import handle

command = 'ol'

from telegram.ext import CommandHandler

handler = CommandHandler(command, handle)
