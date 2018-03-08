# -*- coding: utf-8 -*-
import logging

logger = logging.getLogger(__name__)

from util.common import role_send_text
from util.common import parse_cmd
from service import member_service
from util.common import balance_send_text
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
    # member = member_dao.select_by_teleId(from_user.id)
    # if len(member) == 0:
    #     member_dao.insert(username=from_user.username,
    #                       first_name=from_user.first_name,
    #                       tele_id=from_user.id)
    #     member = member_dao.select_by_teleId(from_user.id)
    # bot.send_message(chat_id=from_user.id,
    #                  text=balance_send_text.format(member[0][1].encode("utf-8"),
    #                                                member[0][3],
    #                                                member[0][0]))


def doing(bot, update):
    cmd, text = parse_cmd(update.message.text)
    id, price = text.split("#")
    member = member_service.select_by_id(id)
    if len(member) == 0:
        update.message.reply_text()
        return ConversationHandler.END
    member = member_service.update_amount(tele_id=member[0][6], price=price, bef=member[0][3])
    from_user = update.message.from_user
    bot.send_message(chat_id=from_user.id,
                     text=balance_send_text.format(member[0][2].encode("utf-8"),
                                                   member[0][3],
                                                   member[0][0]))
    send_text = "管理员为您充值：{0}\n".format(price) + balance_send_text.format(member[0][2].encode("utf-8"),
                                                                         member[0][3],
                                                                         member[0][0])
    bot.send_message(chat_id=member[0][6],
                     text=send_text)
    logger.info('doing over')
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
