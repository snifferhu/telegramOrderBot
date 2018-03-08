# -*- coding: utf-8 -*-
import logging, time, sys

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filename='./log/access_{0}.log'.format(str(time.time())[:6]),
    filemode='a')

# -*- coding: utf-8 -*-
from telegram.ext import Updater

from handlers.help import handler as help_handle
from handlers import error
from handlers import *
import handlers

from telegram.ext import MessageHandler, Filters
logger = logging.getLogger(__name__)


def autoLoadingHandles(dispatcher):
    if handlers == None or handlers.__all__ == None or len(handlers.__all__) == 0:
        logger.info('handles is null')
    else:
        for handle in handlers.__all__:
            logger.info('loading handle:' + handle)
            dispatcher.add_handler(eval(handle + '.handler'))
        dispatcher.add_error_handler(error.handle)
        dispatcher.add_handler(MessageHandler(Filters.command, help_handle))#unknown handle logic


def dispatcher_start(updater):
    dispatcher = updater.dispatcher
    autoLoadingHandles(dispatcher)
    updater.start_polling(poll_interval=1.0, timeout=20)


def main():
    from util.core_config import robot_token
    updater = Updater(token=robot_token)
    try:
        dispatcher_start(updater)
    except:
        logging.info("Unexpected error:", sys.exc_info()[0])
        dispatcher_start(updater)


if __name__ == '__main__':
    main()
