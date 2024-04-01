import asyncio
import os
import logging
import re

import requests

from bs4 import BeautifulSoup

from database.check_in_db import check_url_in_db

logging.basicConfig(
    format="[%(asctime)s]: %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
    level=logging.INFO
)

async def get_parsing_domclick():

    try:
        urls = [
            "https://syktyvkar.domclick.ru/search?deal_type=sale&category=living&offer_type=flat&offer_type=layout&aids=18900&sort=published&sort_dir=desc&is_owner=1&offset=0",
            "https://syktyvkar.domclick.ru/search?deal_type=sale&category=living&offer_type=room&aids=18900&sort=published&sort_dir=desc&is_owner=1&offset=0",
            "https://syktyvkar.domclick.ru/search?deal_type=sale&category=living&offer_type=lot&aids=18900&sort_dir=desc&sort=published&is_owner=1&offset=0",
            "https://syktyvkar.domclick.ru/search?deal_type=sale&category=living&offer_type=house&offer_type=townhouse&aids=18900&sort_dir=desc&sort=published&is_owner=1&offset=0"
        ]

        for url in urls:

            name_page = re.findall(r'offer_type=(.*?)&', url)[0]
            number_page = int(re.findall(r'&offset=(.+)', url)[0]) + 1

            cookies = {
                'qrator_jsid': '1711195733.168.9LLXpF5FciGLRUQh-0n4ulvp48ecm0fnej3db2jsatlc7cqrv',
            }

            params = {
                'deal_type': 'sale',
                'category': 'living',
                'offer_type': [
                    f'{name_page}',
                    'layout',
                ],
                'aids': '18900',
                'sort': 'published',
                'sort_dir': 'desc',
                'is_owner': '1',
                'offset': '0',
            }

            request = requests.get('https://syktyvkar.domclick.ru/search', params=params, cookies=cookies)

            await asyncio.sleep(3)

            try:
                os.mkdir(f"DomClick_Pages")
            except FileExistsError:
                pass

            try:
                os.mkdir(f"DomClick_Pages/{name_page}")
            except FileExistsError:
                pass

            with open(f"DomClick_Pages/{name_page}/{name_page}_{number_page}.html", "w", encoding="utf-8") as file:
                file.write(request.text)
                logging.info(f'Сформирован файл {name_page}_{number_page}.html')

            with open(f"DomClick_Pages/{name_page}/{name_page}_{number_page}.html", "r", encoding="utf-8") as file:
                page = file.read()


            await get_urls(name_page, number_page)

    except KeyboardInterrupt:
        KeyboardInterrupt()

async def get_urls(name_page, number_page):

    try:
        logging.info(f'Переход к get_urls')

        db = ""
        if name_page == "flat":
            db = "urls_apartment_db"

        elif name_page == "house":
            db = "urls_section_db"

        elif name_page == "room":
            db = "urls_rooms_db"

        elif name_page == "lot":
            db = "urls_lands_db"

        urls_in_db, date_in_db = await check_url_in_db(db)

        with open(f"DomClick_Pages/{name_page}/{name_page}_{number_page}.html", 'r', encoding="utf-8") as file:
            page = file.read()

        soup = BeautifulSoup(page, "html.parser")

        get_url_ad = []
        for tag_class in soup.find_all(class_="jIdz3 c1NUU xGMFS"):
            for i in tag_class.find_all("a", class_="NO6xYZ YIdfYp P3YKnR"):
                get_url_ad.append(i.get("href"))

        for i in get_url_ad:
            print(i)


    except KeyboardInterrupt:
        KeyboardInterrupt()


if __name__ == '__main__':
    asyncio.run(get_parsing_domclick())