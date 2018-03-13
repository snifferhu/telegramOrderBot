# -*- coding: utf-8 -*-
import logging, time
from util.common import log_stream_handler
# 将定义好的console日志handler添加到root logger
logging.getLogger(__name__).addHandler(log_stream_handler())
logger = logging.getLogger(__name__)


menu_sleep_mutex = int(time.time()) - 5

def handle(bot, update):
    logger.info("chatId: %s,first_name: %s,text: %s", update.message.chat_id, update.message.from_user.first_name,
                update.message.text)
    global menu_sleep_mutex
    if (int(time.time()) > menu_sleep_mutex + 5):
        menu_photo = open('.\menu\menu.jpg', 'rb')
        bot.send_photo(chat_id=update.message.chat_id, photo=menu_photo, timeout=100)
        menu_photo.close()
        menu_sleep_mutex = int(time.time())
    else:
        bot.send_message(chat_id=update.message.chat_id, text="牛量有限，餐单稍等")


command = 'menu'

from telegram.ext import CommandHandler

handler = CommandHandler(command, handle)
