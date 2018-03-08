# -*- coding: utf-8 -*-
import logging, time

logger = logging.getLogger(__name__)

from lib.common import help_send_text


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
