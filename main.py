import asyncio
import os
import time
import random

from selenium.webdriver.common.by import By
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from check_in_db import append_urls, check_url_in_db

url = "https://www.avito.ru/syktyvkar/kvartiry/prodam-ASgBAgICAUSSA8YQ?s=104"

just_text = ["Новая квартира, 🏃‍♂️ бегооооооом", "Опа-опа-опа - квартира 👾!", "АЛЯРМ 🔔, новая квартира",
             "Там это, квартира новая 👉🏻", "Ну ты там долго 😶, заберут ведь скоро"]


async def pars_html():
    service = Service(executable_path="drive/chromedriver")
    # Нужно чтобы запускать в фоновом режиме без GUI. Скриншоты также будут работать
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")

    # Нужно, чтобы не ждать, пока загрузиться вся страница, типа Js или ещё что-то.
    # Достаточно того, что можно взаимодействовать со страницей
    chrome_options.page_load_strategy = "eager"

    driver = webdriver.Chrome(options=chrome_options)

    driver.get(url)
    assert "Купить" in driver.title

    html = driver.page_source

    try:
        os.mkdir("2avito")
    except FileExistsError:
        pass

    with open(f"2avito/kvartiry_syktyvkar_page_1.html", "w", encoding='utf-8') as file:
        file.write(html)

    with open(f"2avito/kvartiry_syktyvkar_page_1.html", "r", encoding='utf-8') as file:
        page = file.read()

    soup = BeautifulSoup(page, 'html.parser')

    last_page = soup.find_all("span", class_="styles-module-text-InivV")[-1].text

    for i in range(1, int(last_page)):

        try:
            check = driver.find_elements(By.CLASS_NAME, "styles-module-item-kF45w")[-1]
            check.click()

            html = driver.page_source

            print(f"Скачал страницу - {i + 1}")

            with open(f"2avito/kvartiry_syktyvkar_page_{i + 1}.html", "w", encoding='utf-8') as file:
                file.write(html)
        except:
            break

        if i == 3:
            break

    assert "No results found." not in driver.page_source

    driver.close()

    return int(4)


async def get_url(update: Update, context: ContextTypes.DEFAULT_TYPE):
    while True:
        pages = await pars_html()

        time.sleep(3)

        for i in range(0, pages):

            with open(f"2avito/kvartiry_syktyvkar_page_{i+1}.html", "r", encoding='utf-8') as file:
                page = file.read()

            soup = BeautifulSoup(page, 'html.parser')

            urls = []
            for j in soup.find_all("a", class_="iva-item-sliderLink-uLz1v"):
                urls.append(f"https://www.avito.ru{j.get('href')}")

            for j in urls:

                if j not in await check_url_in_db():
                    await append_urls(j)
                    random_text = random.choice(just_text)
                    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"{random_text} - {j}")
                    await asyncio.sleep(3)

                else:
                    pass

        await asyncio.sleep(300)


if __name__ == '__main__':
    asyncio.run(pars_html())
    # asyncio.run(get_url())
