# -*- coding: utf-8 -*-
import logging
from util.common import log_stream_handler, deposit_send_text

# 将定义好的console日志handler添加到root logger
logging.getLogger(__name__).addHandler(log_stream_handler())
logger = logging.getLogger(__name__)

from util.common import role_send_text
from util.common import parse_cmd
from service import member_service, balance_service
from util.common import deposit_notice_text

DOING, DONE = range(2)


def deposit(bot, update):
    logger.info("chatId: %s,first_name: %s,text: %s", update.message.chat_id, update.message.from_user.first_name,
                update.message.text)
    from_user = update.message.from_user
    if from_user.id != 427009122:
        bot.send_message(chat_id=from_user.id,
                         text=role_send_text)
        return ConversationHandler.END
    bot.send_message(chat_id=from_user.id,
                     text=deposit_notice_text)
    return DOING


def doing(bot, update):
    try:
        from_user = update.message.from_user
        cmd, text = parse_cmd(update.message.text)
        if text.find('#') == -1:
            update.message.reply_text()
            return ConversationHandler.END

        id, price = text.split("#")
        member = member_service.select_by_id(id)
        logger.info("member:%s", member)
        if len(member) == 0:
            update.message.reply_text()
            return ConversationHandler.END
        balance_service.update_amount(tele_id=member[0]["tele_id"],
                                      price=price,
                                      driver_tele_id=from_user.id)

        send_text = balance_service.select_by_tele_id(member[0], from_user.id)
        bot.send_message(chat_id=from_user.id,
                         text=send_text)
        send_text = deposit_send_text.format(from_user.first_name, price) + send_text

        bot.send_message(chat_id=member[0]['tele_id'],
                         text=send_text)
        logger.info('doing over')
        return ConversationHandler.END
    except:
        return ConversationHandler.END


def cancel(bot, update):
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text('再见! 期待下一次的合作.')
    return ConversationHandler.END


command = 'deposit'

from telegram.ext import ConversationHandler, CommandHandler, Filters, MessageHandler

handler = ConversationHandler(
    entry_points=[CommandHandler("deposit", deposit)],

    states={
        DOING: [MessageHandler(Filters.text, doing)]
    },

    fallbacks=[CommandHandler('cancel', cancel)]
)
