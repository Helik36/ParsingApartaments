import asyncio
import random

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import logging
from config.config import API, MY_ID
from database.check_in_db import append_users_id_telegram, get_users_id_telegram, get_new_url_from_pars, detele_new_url

from data_Avito import pars_html

token = API
my_id = MY_ID

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

BUTTON = range(1)

# Сюда передаётся именно как (context: ContextTypes.DEFAULT_TYPE)
async def send_message_about_new_url(context: ContextTypes.DEFAULT_TYPE):

    user_id = await get_users_id_telegram()
    new_urls = await get_new_url_from_pars()

    if not new_urls:
        pass
    else:
        for id_user_telegram in user_id:
            for url in new_urls:
                just_text = []

                if "kvartiry" in url.split("/")[4]:
                    just_text = ["Новая квартира, 🏃‍♂️ бегооооооом", "Опа-опа-опа - квартира!👾",
                                 "АЛЯРМ 🔔, новая квартира",
                                 "Там это, квартира новая 👉🏻", "Ну ты там долго 😶, заберут ведь скоро"]

                elif "doma_dachi_kottedzhi" in url.split("/")[4]:
                    just_text = ["🏠Новый дом", "🏗Дом", "🔔Новое объявление дома",
                                 "Объявление дома/дачи/коттетджа/чеготамещё 👉🏻"]


                elif "komnaty" in url.split("/")[4]:
                    just_text = ["⛺️Новая комната", "🗿Новая cumната", "Объявление комнаты 👉🏻",
                                 "🔔Новое объявление комнаты"]

                elif "zemelnye_uchastki" in url.split("/")[4]:

                    just_text = ["🌅Новое объявление участка", "Новый участок", "Объявление участка 👉🏻",
                                 "🔔Новое объявление участка"]

                random_text = random.choice(just_text)
                await context.bot.send_message(chat_id=id_user_telegram, text=f'{random_text} - {url}')

        await detele_new_url()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id

    if str(chat_id) in await get_users_id_telegram():
        pass
    else:
        await append_users_id_telegram(chat_id)

    await context.bot.send_message(chat_id=update.effective_chat.id, text="LEEET'S FUUUUUCKKIIIIING GOOOOOOO!!!!")
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo="image/pap.jpg")

    # Чтобы работало, нужно скачать pip install python-telegram-bot[job-queue]
    # Далее она позволяет выполнять задачи с задержкой или даже периодически, с заданным интервалом.
    context.job_queue.run_repeating(send_message_about_new_url, interval=180, chat_id=chat_id)


async def main():
    app = Application.builder().token(token).concurrent_updates(True).build()

    app.add_handler(CommandHandler("start", start))

    task1 = pars_html()
    tasks = [task1]

    try:
        async with app:
            await app.initialize()
            await app.start()
            await app.updater.start_polling()
            await asyncio.gather(*tasks)
    except:
        KeyboardInterrupt()


if __name__ == '__main__':
    asyncio.run(main())
