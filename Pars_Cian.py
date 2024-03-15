import asyncio
import time

import requests
from bs4 import BeautifulSoup


async def get_pages_cian():
    url = "https://syktyvkar.cian.ru/cat.php?deal_type=sale&engine_version=2&offer_seller_type%5B0%5D=2&offer_type=flat&p=1&region=5006&room1=1&room2=1&room3=1&room4=1&room5=1&room6=1&sort=creation_date_desc"

    request = requests.get(url)

    number_page = url.split('&')[4]

    with open(f"Cian_Pages/apartaments_{number_page}.html", "w", encoding="utf-8") as file:
        file.write(request.text)

    with open(f"Cian_Pages/apartaments_{number_page}.html", "r", encoding="utf-8") as file:
        page = file.read()

    soup = BeautifulSoup(page, "html.parser")

    next_page = soup.find_all("a",
                              class_="_93444fe79c--button--KVooB _93444fe79c--link-button--ujZuh _93444fe79c--M--I5Xj6 _93444fe79c--button--WChcG")

    await asyncio.sleep(3)

    while True:
        if next_page[-1].find("span").text == "Дальше":
            if "https://syktyvkar.cian.ru" in next_page[-1].get("href"):
                url = next_page[-1].get("href")

            else:
                url = f"https://syktyvkar.cian.ru{next_page[-1].get("href")}"

            number_page = url.split('&')[4]

            request = requests.get(url)

            with open(f"Cian_Pages/apartaments_{number_page}.html", "w", encoding="utf-8") as file:
                file.write(request.text)

            with open(f"Cian_Pages/apartaments_{number_page}.html", "r", encoding="utf-8") as file:
                page = file.read()

            soup = BeautifulSoup(page, "html.parser")

            next_page = soup.find_all("a",
                                      class_="_93444fe79c--button--KVooB _93444fe79c--link-button--ujZuh _93444fe79c--M--I5Xj6 _93444fe79c--button--WChcG")

            await asyncio.sleep(3)

        else:
            print("Выход из цикла")
            break


async def get_urls():
    pass


if __name__ == '__main__':
    asyncio.run(get_pages_cian())
