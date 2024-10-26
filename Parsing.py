import asyncio
import os
import logging
import requests
from bs4 import BeautifulSoup

from database.check_in_db import append_urls, check_url_in_db, append_new_url_from_pars

logging.basicConfig(
    format="[%(asctime)s]: %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
    level=logging.INFO)


class ParsingSites:
    def __init__(self, urls, current_panel, class_ads, **args):
        self.urls = urls
        self.current_panel = current_panel
        self.class_ads = class_ads
        self.args = args

    async def parsing_page(self, proxies=None):

        await asyncio.sleep(0)

        for url in self.urls:

            if proxies is None:
                request = requests.get(url, cookies=self.args["cookies"], headers=self.args["headers"])

            else:
                request = requests.get(url, cookies=self.args["cookies"], headers=self.args["headers"], proxies=proxies)

            logging.info(f'{request.status_code}')
            html = request.text

            site = url.split("/")[2].split(".")[1]

            type_search = ""
            if site == "avito":
                type_search = f"{url.split('/')[4]}"
            elif site == "cian":
                type_search = f"{url.split('/')[3]}"

            main_folder = f"Pages_{site}"
            name_page_html = f"{type_search}_page.html"

            try:
                os.mkdir(main_folder)
            except FileExistsError:
                pass

            try:
                os.mkdir(f"{main_folder}/{type_search}")
            except FileExistsError:
                pass

            with open(f"{main_folder}/{type_search}/{name_page_html}", "w", encoding="utf-8") as file:
                file.write(html)
                logging.info(f'Сформирован файл {name_page_html}')

            # return type_search, f"{main_folder}/{type_search}/{name_page_html}"

            logging.info(f'Переход к get_urls')
            await asyncio.sleep(0)

            db = ""
            if type_search in ["kupit-kvartiru", "kvartiry"]:
                db = "urls_apartment_db"

            elif type_search in ["kupit-dom", "doma_dachi_kottedzhi"]:
                db = "urls_section_db"

            elif type_search in ["kupit-komnatu-bez-posrednikov", "komnaty"]:
                db = "urls_rooms_db"

            elif type_search in ["kupit-zemelniy-uchastok", "zemelnye_uchastki"]:
                db = "urls_lands_db"

            urls_in_db, date_in_db = await check_url_in_db(db, "database/base_urls.db")

            with open(f"{main_folder}/{type_search}/{name_page_html}", 'r', encoding="utf-8") as file:
                page = file.read()

            soup = BeautifulSoup(page, "html.parser")

            get_href = []
            # Делаем выборку только по выбранным фильтрам
            for tag_class in soup.find(class_=self.current_panel):

                # Проходимся по массиву и забираем теги а
                for tag_a in tag_class.find_all("a", class_=self.class_ads):

                    if site == "avito":
                        avito_url = "https://www.avito.ru" + tag_a.get("href")
                        get_href.append(avito_url)

                    else:
                        get_href.append(tag_a.get("href"))

            for new_url in get_href:
                if new_url not in urls_in_db:
                    await append_urls(new_url, db, "database/base_urls.db")
                    await append_new_url_from_pars(new_url, "database/base_urls.db")
                    logging.info(f"Добавлен {new_url}")

                # Если после длительной остановки нужно обновить полностью БД, на 1 запуск убрать нижние 2 строчки
                else:

                    break

            await asyncio.sleep(15)
