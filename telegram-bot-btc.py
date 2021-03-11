from telegram import *
from telegram.ext import *
import logging
import requests 

## NO usar agregar la variable bot en las funciones ()

# Logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


def valor(update, context):
    btc = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    precio = btc.json()['bpi']['USD']['rate']
    update.message.reply_text(precio)


def main():
    # Create updater and pass in Bot's auth key.
    updater = Updater(token='XXXXXXXXXX', use_context=True)
    # Get dispatcher to register handlers
    dispatcher = updater.dispatcher
    # answer commands
    dispatcher.add_handler(CommandHandler('valor', valor))
    # start the bot
    updater.start_polling()
    # Stop
    updater.idle()

if __name__ == '__main__':
    main()
