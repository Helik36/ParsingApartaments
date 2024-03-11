import asyncio
import logging
import os
import random

from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from telegram.ext import ContextTypes

from check_in_db import append_urls, check_url_in_db

logging.basicConfig(level=logging.DEBUG)

urls_pars = ["https://www.avito.ru/syktyvkar/kvartiry/prodam-ASgBAgICAUSSA8YQ?f=ASgBAgICAkSSA8YQkL4Nlq41&s=104",
             "https://www.avito.ru/syktyvkar/doma_dachi_kottedzhi/prodam-ASgBAgICAUSUA9AQ?cd=1&p=1&s=104&user=1",
             "https://www.avito.ru/syktyvkar/komnaty/prodam-ASgBAgICAUSQA7wQ?cd=1&localPriority=1&s=104&user=1",
             "https://www.avito.ru/syktyvkar/zemelnye_uchastki/prodam-ASgBAgICAUSWA9oQ?cd=1&s=104&user=1"]


async def pars_html(context: ContextTypes.DEFAULT_TYPE):
    service = Service(executable_path="driver/chromedriver-linux64/chromedriver")
    # Нужно, чтобы запускать в фоновом режиме без GUI. Скриншоты также будут работать
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")

    # Нужно, чтобы не ждать, пока загрузиться вся страница, типа Js или ещё что-то.
    # Достаточно того, что можно взаимодействовать со страницей
    # normal - Used by default, waits for all resources to download
    # eager	 - DOM access is ready, but other resources like images may still be loading
    # none   -Does not block WebDriver at all
    chrome_options.page_load_strategy = "eager"
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    count = 1
    for url in urls_pars:
        driver = webdriver.Chrome(options=chrome_options)
        try:
            logging.basicConfig(level=logging.DEBUG)
            driver.get(url)
            assert "Купить" in driver.title

            html = driver.page_source

            print(f"{count}{url.split('/')}\n{count}{url.split('/')[4]}")
            try:
                os.mkdir(f"{count}{url.split('/')[4]}")
            except FileExistsError:
                pass

            name_html = f"{count}{url.split('/')[4]}/{url.split('/')[4]}"

            with open(f"{name_html}_page_1.html", "w", encoding='utf-8') as file:
                file.write(html)

            with open(f"{name_html}_page_1.html", "r", encoding='utf-8') as file:
                page = file.read()

            soup = BeautifulSoup(page, 'html.parser')

            last_page = soup.find_all("span", class_="styles-module-text-InivV")[-1].text

            for i in range(1, int(last_page)):

                try:
                    check = driver.find_elements(By.CLASS_NAME, "styles-module-item-kF45w")[-1]
                    check.click()

                    html = driver.page_source

                    with open(f"{name_html}_page_{i + 1}.html", "w",
                              encoding='utf-8') as file:
                        file.write(html)

                except FileNotFoundError:
                    print("Возникла ошибка при сохранений файла")
                    break

                if i == 1:
                    break

            assert "No results found." not in driver.page_source

            driver.close()

            await get_apartments_url(context, int(1), name_html)

            count += 1

        except:
            print("Возникла ошибка.")
            driver.close()


# Сюда передаётся именно как (context: ContextTypes.DEFAULT_TYPE)
async def get_apartments_url(context: ContextTypes.DEFAULT_TYPE, pages, name_html):

    db = ""
    just_text = []

    if "kvartiry" in name_html:
        db = "urls_apartment_db"
        just_text = ["Новая квартира, 🏃‍♂️ бегооооооом", "Опа-опа-опа - квартира!👾", "АЛЯРМ 🔔, новая квартира",
                     "Там это, квартира новая 👉🏻", "Ну ты там долго 😶, заберут ведь скоро"]

    elif "doma_dachi_kottedzhi" in name_html:
        db = "urls_section_db"
        just_text = ["🏠Новый дом", "🏗Дом",  "🔔Новое объявление дома", "Объявление дома/дачи/коттетджа/чеготамещё 👉🏻"]


    elif "komnaty" in name_html:
        db = "urls_rooms_db"
        just_text = ["⛺️Новая комната", "🗿Новая cumната", "Объявление комнаты 👉🏻", "🔔Новое объявление комнаты"]

    elif "zemelnye_uchastki" in name_html:
        db = "urls_lands_db"
        just_text = ["🌅Новое объявление участка", "Новый участок", "Объявление участка 👉🏻", "🔔Новое объявление участка"]

    urls_from_db, date_from_db = await check_url_in_db(db)

    for number_page in range(0, int(pages)):

        with open(f"{name_html}_page_{number_page + 1}.html", "r", encoding='utf-8') as file:
            page = file.read()

        soup = BeautifulSoup(page, 'html.parser')

        new_urls = []
        for href in soup.find_all("a", class_="iva-item-sliderLink-uLz1v"):
            new_urls.append(f"https://www.avito.ru{href.get('href')}")

        for new_url in new_urls:
            if new_url not in urls_from_db:
                await append_urls(new_url, db)
                random_text = random.choice(just_text)
                await context.bot.send_message(chat_id=context.job.chat_id, text=f"{random_text} - {new_url}")
                await asyncio.sleep(2)

            else:
                pass

    await asyncio.sleep(60)

