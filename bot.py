from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import logging
from config import API, MY_ID
from main import get_url

token = API
my_id = MY_ID

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="LEEET'S FUUUUUCKKIIIIING GOOOOOOO!!!!")
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo="pap.jpg")
    await get_url(update, context)

if __name__ == '__main__':

    app = Application.builder().token(token).build()

    start_handler = CommandHandler('start', start)
    app.add_handler(start_handler)

    app.run_polling()
