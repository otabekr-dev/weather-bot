from config import TOKEN
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
)
import handlers

def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', handlers.start))

    dispatcher.add_handler(MessageHandler(Filters.location, handlers.send_weather_by_location))


    updater.start_polling()
    updater.idle()

main()    