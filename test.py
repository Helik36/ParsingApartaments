import asyncio
import datetime

from check_in_db import check_url_in_db


async def test():
    urls_db, dates_db = await check_url_in_db("urls_apartment_db")
    urls = urls_db
    dates = dates_db

    for url in range(len(urls)):
        print(f"{dates[url]} - {urls[url]}")

    print("\n\n")

    urls_db, dates_db = await check_url_in_db("urls_section_db")
    urls = urls_db
    dates = dates_db

    for url in range(len(urls)):
        print(f"{dates[url]} - {urls[url]}")


    print("\n\n")

    urls_db, dates_db = await check_url_in_db("urls_rooms_db")
    urls = urls_db
    dates = dates_db

    for url in range(len(urls)):
        print(f"{dates[url]} - {urls[url]}")





    # print(datetime.datetime.now().strftime("%d-%m-%Y %H:%M"))

    # urls_pars = ["https://www.avito.ru/syktyvkar/kvartiry/prodam-ASgBAgICAUSSA8YQ?f=ASgBAgICAkSSA8YQkL4Nlq41&s=104",
    #              "https://www.avito.ru/syktyvkar/doma_dachi_kottedzhi/prodam-ASgBAgICAUSUA9AQ?cd=1&p=1&s=104&user=1",
    #              "https://www.avito.ru/syktyvkar/komnaty/prodam-ASgBAgICAUSQA7wQ?cd=1&localPriority=1&s=104&user=1"]
    #
    # print(urls_pars[0].split("/"))



if __name__ == '__main__':
    asyncio.run(test())
