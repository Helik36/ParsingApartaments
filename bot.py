from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import logging
from config import API, MY_ID

from pars import pars_html

token = API
my_id = MY_ID

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

BUTTON = range(1)


# Сюда передаётся именно как (context: ContextTypes.DEFAULT_TYPE)
async def buba(context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=context.job.chat_id, text=f'BEEP!')


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id

    await context.bot.send_message(chat_id=update.effective_chat.id, text="LEEET'S FUUUUUCKKIIIIING GOOOOOOO!!!!")
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo="image/pap.jpg")

    # Чтобы эта штука работа, нужно скачать pip install python-telegram-bot[job-queue]
    # Далее она позволяет выполнять задачи с задержкой или даже периодически, с заданным интервалом.
    # context.job_queue.run_repeating(buba, 60, chat_id=chat_id)
    # context.job_queue.run_repeating(get_apartments_url, 180, chat_id=chat_id)
    # context.job_queue.run_repeating(get_section_url, 180, chat_id=chat_id)
    context.job_queue.run_repeating(pars_html, 180, chat_id=chat_id)


if __name__ == '__main__':
    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))

    app.run_polling()
