# -*- coding: utf-8 -*-
import logging

logger = logging.getLogger(__name__)

from handlers.balance import handle

command = 'bal'

from telegram.ext import CommandHandler

handler = CommandHandler(command, handle)
