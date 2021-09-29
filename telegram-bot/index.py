#!/usr/bin/env python

import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from FileManager.index import save_user

BOT_TOKEN = '2048360234:AAHwmUQUEZUf9Jhc7JCg37vJAOUwAOBQ-rU'

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def new_chat_member(update, context):
    members = update.message.new_chat_members
    for member in members:
        msg = 'Olá {}, seja bem-vindo(a) ao grupo dos subs do FRT. Por favor, digite seu nick da Twitch para que possamos verificar se o seu sub está ativo. Você tem 03 minutos para responder essa mensagem.'.format(member.first_name)
        update.message.reply_text(msg)

def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    updater = Updater(BOT_TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, new_chat_member))

    dp.add_error_handler(error)
    
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
