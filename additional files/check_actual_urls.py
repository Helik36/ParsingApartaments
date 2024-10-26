import asyncio

from database.check_in_db import check_url_in_db


async def check_db():

    """
    Просто чтобы проверять ссылки
    :return:
    """

    urls_db, dates_db = await check_url_in_db("urls_apartment_db", "../database/base_urls.db")

    urls = urls_db
    dates = dates_db

    with open("check_urls.txt", "w") as file:
        file.write("Квартиры:\n")

    for url in range(len(urls)):
        with open("check_urls.txt", "a") as file:
            file.write(f"{dates[url]} - {urls[url]}\n")

    urls_db, dates_db = await check_url_in_db("urls_section_db", "../database/base_urls.db")
    urls = urls_db
    dates = dates_db

    with open("check_urls.txt", "a") as file:
        file.write("\n\nЗемельный участок:\n")

    for url in range(len(urls)):
        with open("check_urls.txt", "a") as file:
            file.write(f"{dates[url]} - {urls[url]}\n")

    urls_db, dates_db = await check_url_in_db("urls_rooms_db", "../database/base_urls.db")
    urls = urls_db
    dates = dates_db

    with open("check_urls.txt", "a") as file:
        file.write("\n\nКомнаты:\n")

    for url in range(len(urls)):
        with open("check_urls.txt", "a") as file:
            file.write(f"{dates[url]} - {urls[url]}\n")

if __name__ == '__main__':

    asyncio.run(check_db())