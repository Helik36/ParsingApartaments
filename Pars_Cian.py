import asyncio
import os
import logging
import requests

from bs4 import BeautifulSoup

from check_in_db import append_urls, check_url_in_db, append_new_url_from_pars

logging.basicConfig(
    format="[%(asctime)s]: %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
    level=logging.INFO
)


async def get_pages_cian():
    urls = [
        "https://syktyvkar.cian.ru/kupit-kvartiru/?deal_type=sale&engine_version=2&offer_seller_type%5B0%5D=2&offer_type=flat&p=1&region=5006&room1=1&room2=1&room3=1&room4=1&room5=1&room6=1&sort=creation_date_desc",
        "https://syktyvkar.cian.ru/kupit-komnatu-bez-posrednikov/?deal_type=sale&engine_version=2&is_by_homeowner=1&offer_type=flat&p=1&region=5006&room0=1&sort=creation_date_desc",
        "https://syktyvkar.cian.ru/kupit-zemelniy-uchastok/?deal_type=sale&engine_version=2&object_type%5B0%5D=3&offer_seller_type%5B0%5D=2&offer_type=suburban&p=1&region=5006&sort=creation_date_desc",
        # "https://syktyvkar.cian.ru/kupit-dom/?deal_type=sale&engine_version=2&object_type%5B0%5D=1&offer_seller_type%5B0%5D=2&offer_type=suburban&p=1&region=5006&sort=creation_date_desc"
        # Плохр работает
    ]

    for url in urls:
        try:
            request = requests.get(url)
            name_page = url.split("/")[3]
            number_page = url.split('&')[4]

            try:
                os.mkdir(f"Cian_Pages/{name_page}")
            except FileExistsError:
                pass

            with open(f"Cian_Pages/{name_page}/{name_page}_{number_page}.html", "w", encoding="utf-8") as file:
                file.write(request.text)
                logging.info(f'Сформирован файл {name_page}_{number_page}.html')

            with open(f"Cian_Pages/{name_page}/{name_page}_{number_page}.html", "r", encoding="utf-8") as file:
                page = file.read()

            soup = BeautifulSoup(page, "html.parser")

            next_page = soup.find_all("a", class_="_93444fe79c--button--KVooB _93444fe79c--link-button--ujZuh _93444fe79c--M--I5Xj6 _93444fe79c--button--WChcG")

            await asyncio.sleep(3)

            while True:

                if not next_page:
                    await get_urls(name_page)
                    await asyncio.sleep(5)
                    break

                elif next_page[-1].find("span").text == "Дальше":
                    if "https://syktyvkar.cian.ru" in next_page[-1].get("href"):
                        url = next_page[-1].get("href")

                    else:
                        url = f"https://syktyvkar.cian.ru{next_page[-1].get("href")}"

                    number_page = url.split('&')[4]

                    request = requests.get(url)

                    with open(f"Cian_Pages/{name_page}/{name_page}_{number_page}.html", "w", encoding="utf-8") as file:
                        file.write(request.text)
                        logging.info(f'Сформирован файл {name_page}_{number_page}.html')

                    with open(f"Cian_Pages/{name_page}/{name_page}_{number_page}.html", "r", encoding="utf-8") as file:
                        page = file.read()

                    soup = BeautifulSoup(page, "html.parser")

                    next_page = soup.find_all("a", class_="_93444fe79c--button--KVooB _93444fe79c--link-button--ujZuh _93444fe79c--M--I5Xj6 _93444fe79c--button--WChcG")

                    await asyncio.sleep(3)

                else:
                    logging.info(f'Выход из цикла')
                    await get_urls(name_page)
                    await asyncio.sleep(5)
                    break

        except KeyboardInterrupt:
            KeyboardInterrupt()
            logging.info(f'Работа завершена')

    logging.info(f'Цикл завершён')


async def get_urls(name_page):
    try:
        logging.info(f'Переход к get_urls')

        db = ""
        if name_page == "kupit-kvartiru":
            db = "urls_apartment_db"

        elif name_page == "kupit-dom":
            db = "urls_section_db"

        elif name_page == "kupit-komnatu-bez-posrednikov":
            db = "urls_rooms_db"

        elif name_page == "kupit-zemelniy-uchastok":
            db = "urls_lands_db"

        urls_in_db, date_in_db = await check_url_in_db(db)

        with open(f"Cian_Pages/{name_page}/{os.listdir(f"Cian_Pages/{name_page}")[0]}", 'r', encoding="utf-8") as file:
            page = file.read()

        soup = BeautifulSoup(page, "html.parser")

        get_url_ad = []
        # Делаем выборку только по выбранным фильтрам (без предложения циана об осмотре других объявлений
        for tag_class in soup.find(class_="_93444fe79c--wrapper--W0WqH"):

            # Проходимся по массиву и забираем теги а
            for tag_a in tag_class.find_all("a", class_="_93444fe79c--link--VtWj6"):
                get_url_ad.append(tag_a.get("href"))

        for url in get_url_ad:
            if url not in urls_in_db:
                await append_urls(url, db)
                # await append_new_url_from_pars(url)
                logging.info(f"Добавлен {url}")
            else:
                logging.info(f"Добавлять нечего")
                break

    except KeyboardInterrupt:
        KeyboardInterrupt()
if __name__ == '__main__':
    asyncio.run(get_pages_cian())
    # asyncio.run(get_urls())
