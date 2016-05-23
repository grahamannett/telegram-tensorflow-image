from uuid import uuid4
from configparser import ConfigParser
import random
import re

from telegram import InlineQueryResultArticle, ParseMode, \
    InputTextMessageContent
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import logging

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

logger = logging.getLogger(__name__)

vids = [
    'https://www.youtube.com/watch?v=5pGJCkCDK5A',
    'https://www.youtube.com/watch?v=iaFa0sYjId8',
    'https://www.youtube.com/watch?v=gMkc_BHR5PA',
    'https://www.youtube.com/watch?v=sUcr24DFxvA',
    'https://www.youtube.com/watch?v=qAkETBkl-zc',
    'https://www.youtube.com/watch?v=h8growuncz0',
    'https://www.youtube.com/watch?v=XzDp1H1mBmk',
    'https://www.youtube.com/watch?v=S89srrSQ3Jk']

msg = 'tell em: '


def get_config_tokn():
    config = ConfigParser()
    config.read_file(open('config'))
    token = config['default']['token']
    return token

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
# def start(bot, update):
#     bot.sendMessage(update.message.chat_id, text='Hi!')


def tellem(bot, update):
    bot.sendMessage(update.message.chat_id, text=msg + random.choice(vids))


def escape_markdown(text):
    """Helper function to escape telegram markup symbols"""
    escape_chars = '\*_`\['
    return re.sub(r'([%s])' % escape_chars, r'\\\1', text)


def inlinequery(bot, update):
    query = update.inline_query.query
    results = list()
    # results.append(InlineQueryResultArticle(
    #     id=uuid4(),
    #     title="Caps",
    #     input_message_content=InputTextMessageContent(query.upper())))
    # results.append(InlineQueryResultArticle(
    #     id=uuid4(),
    #     title="Bold",
    #     input_message_content=InputTextMessageContent(
    #         "*%s*" % escape_markdown(query),
    #         parse_mode=ParseMode.MARKDOWN)))

    results.append(InlineQueryResultArticle(
        id=uuid4(),
        title="tell em",
        input_message_content=InputTextMessageContent(msg +
                                                      random.choice(vids))))

    bot.answerInlineQuery(update.inline_query.id, results=results)


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater(get_config_tokn())

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    # dp.addHandler(CommandHandler("start", start))
    dp.addHandler(CommandHandler("tellem", tellem))

    # on noncommand i.e message - echo the message on Telegram
    dp.addHandler(InlineQueryHandler(inlinequery))

    # log all errors
    dp.addErrorHandler(error)

    # Start the Bot
    updater.start_polling()

    # Block until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
