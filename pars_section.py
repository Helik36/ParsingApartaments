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

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

url = "https://www.avito.ru/syktyvkar/doma_dachi_kottedzhi/prodam-ASgBAgICAUSUA9AQ?cd=1&p=1&s=104&user=1"


async def pars_html():
    service = Service(executable_path="drive/chromedriver-linux64/chromedriver")
    # Нужно чтобы запускать в фоновом режиме без GUI. Скриншоты также будут работать
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

    driver = webdriver.Chrome(options=chrome_options)

    # try:
    driver.get(url)
    assert "Купить" in driver.title

    html = driver.page_source

    try:
        os.mkdir("2section")
    except FileExistsError:
        pass

    with open(f"2section/doma_dachi_kottedzhi_page_1.html", "w", encoding='utf-8') as file:
        file.write(html)
    print(f"Скачал страницу участков - 1")

    with open(f"2section/doma_dachi_kottedzhi_page_1.html", "r", encoding='utf-8') as file:
        page = file.read()

    soup = BeautifulSoup(page, 'html.parser')

    last_page = soup.find_all("span", class_="styles-module-text-InivV")[-1].text

    for i in range(1, int(last_page)):

        try:
            check = driver.find_elements(By.CLASS_NAME, "styles-module-item-kF45w")[-1]
            check.click()

            html = driver.page_source

            print(f"Скачал страницу участков - {i + 1}")

            with open(f"2section/doma_dachi_kottedzhi_page_{i + 1}.html", "w", encoding='utf-8') as file:
                file.write(html)
        except:
            print("Возникла ошибка при сохранений файла")
            break

        if i == 1:
            break

    assert "No results found." not in driver.page_source

    driver.close()

    return int(2)
    # return int(last_page)

# except:
# print("Возникла ошибка")
# driver.close()


# Сюда передаётся именно как (context: ContextTypes.DEFAULT_TYPE)
async def get_section_url(context: ContextTypes.DEFAULT_TYPE):
    pages = await pars_html()

    urls_from_db, date_from_db = await check_url_in_db("urls_section_db")
    for number_page in range(0, int(pages)):

        with open(f"2section/doma_dachi_kottedzhi_page_{number_page + 1}.html", "r", encoding='utf-8') as file:
            page = file.read()

        soup = BeautifulSoup(page, 'html.parser')

        new_urls = []
        for href in soup.find_all("a", class_="iva-item-sliderLink-uLz1v"):
            new_urls.append(f"https://www.avito.ru{href.get('href')}")

        for new_url in new_urls:
            if new_url not in urls_from_db:
                print(f"Добавил участок - {new_url}")
                await append_urls(new_url, "urls_section_db")
                await context.bot.send_message(chat_id=context.job.chat_id,
                                               text=f"🏡 Новая дача/дом/коттедж/таунхаус - {new_url}")
                await asyncio.sleep(2)

            else:
                pass


async def append_urls_in_db():
    pages = await pars_html()

    urls_from_db, date_from_db = await check_url_in_db("urls_section_db")
    for number_page in range(0, int(pages)):

        with open(f"2section/doma_dachi_kottedzhi_page_{number_page + 1}.html", "r", encoding='utf-8') as file:
            page = file.read()

        soup = BeautifulSoup(page, 'html.parser')

        new_urls = []
        for href in soup.find_all("a", class_="iva-item-sliderLink-uLz1v"):
            new_urls.append(f"https://www.avito.ru{href.get('href')}")

        for new_url in new_urls:
            if new_url not in urls_from_db:
                print(f"Добавил - {new_url}")
                await append_urls(new_url, "urls_section_db")
            else:
                pass


if __name__ == '__main__':
    asyncio.run(append_urls_in_db())
