import asyncio
import datetime

from check_in_db import check_url_in_db


async def test():
    url, date = await check_url_in_db("urls_apartment_db")
    for i in url:
        # print(f"{i[0]} \t\t\t- {i[1]}")
        print(i)

    # print(url)


    # print(datetime.datetime.now().strftime("%d-%m-%Y %H:%M"))


if __name__ == '__main__':
    asyncio.run(test())
