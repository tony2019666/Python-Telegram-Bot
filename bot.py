#!/usr/bin/env python

import logging

from telegram import Update, ParseMode
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, MessageHandler, Filters

import Commands.search as SearchCommand
import Commands.today as TodayCommand

# Telegram Bot Token
bot_token = ''
# TMDB APIKey
tmdb_apikey = ''
tmdb_timeout = 5

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO, filename='recording.log', filemode='a'
)

logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext) -> None:
    try:
        text = '聊天框输入内容即可搜索指定的剧集/电影\n*更多功能还在开发/优化中..\n使用问题联系：@dyaxy*'
        update.message.reply_markdown(text)

    except Exception as error:
        logging.error(error)


def today(update: Update, context: CallbackContext) -> None:
    try:
        text, reply_markup = TodayCommand.onTrending('today')
        update.message.reply_markdown(
            text, reply_markup=reply_markup)

    except Exception as error:
        logging.error(error)


def search(update: Update, context: CallbackContext) -> None:
    try:
        m = update.message
        text, reply_markup = SearchCommand.onSearch(m.text)
        m.reply_markdown(
            text, reply_markup=reply_markup)
        logging.info(f'{m.chat.id}@{m.chat.username} - {m.text}')
    except Exception as error:
        logging.error(error)


def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    bot = query.bot
    calldata = query.data.split('_')
    calltype = calldata[0]
    match calltype:
        case 'again':
            text, reply_markup = SearchCommand.onSearch(
                calldata[1])
            query.edit_message_text(
                text=text,
                reply_markup=reply_markup,
                parse_mode=ParseMode.MARKDOWN
            )
        case 'search':
            text, reply_markup = SearchCommand.onSearchResult(
                calldata[1], calldata[2])
            query.edit_message_text(
                text=text,
                reply_markup=reply_markup,
                parse_mode=ParseMode.MARKDOWN
            )
        case 'info':
            text, reply_markup = SearchCommand.onInfomation(
                calldata[1], calldata[2], calldata[3])
            query.edit_message_text(
                text=text,
                reply_markup=reply_markup,
                parse_mode=ParseMode.MARKDOWN
            )
        case 'watch':
            message = bot.send_message(
                chat_id=update.effective_message.chat_id,
                text='正在搜索可用的国家或地区...',
                parse_mode=ParseMode.MARKDOWN
            )
            text, reply_markup = SearchCommand.onSelectCountry(
                calldata[1], calldata[2])
            bot.edit_message_text(
                chat_id=update.effective_message.chat_id,
                text=text,
                message_id=message.message_id,
                reply_markup=reply_markup,
                parse_mode=ParseMode.MARKDOWN
            )
        case 'country':
            offer, providers = SearchCommand.onOffer(
                calldata[1], calldata[2], calldata[3])
            dictlist = SearchCommand.onOfferConvert(offer, providers)
            for i in dictlist:
                text, reply_markup = SearchCommand.onOfferSender(
                    dictlist[i], i, calldata[1])
                message = bot.send_message(
                    chat_id=update.effective_message.chat_id,
                    text=text,
                    reply_markup=reply_markup,
                    parse_mode=ParseMode.MARKDOWN
                )
    logging.info(f'{query.message.chat.id}@{query.message.chat.username} - {query.data}')


def main() -> None:
    updater = Updater(bot_token)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("s", start))
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("today", today))
    dispatcher.add_handler(CallbackQueryHandler(button))
    dispatcher.add_handler(MessageHandler(
        Filters.text & ~Filters.command, search))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
