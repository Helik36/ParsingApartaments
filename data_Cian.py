import asyncio
import logging
from Parsing import ParsingPages

logging.basicConfig(
    format="[%(asctime)s]: %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
    level=logging.INFO)

current_panel = "_93444fe79c--wrapper--W0WqH"
class_ads = "_93444fe79c--link--VtWj6"


async def get_pages_cian():

    while True:

        urls_pars = [
            "https://syktyvkar.cian.ru/kupit-kvartiru/?deal_type=sale&engine_version=2&offer_seller_type%5B0%5D=2&offer_type=flat&p=1&region=5006&room1=1&room2=1&room3=1&room4=1&room5=1&room6=1&sort=creation_date_desc",
            "https://syktyvkar.cian.ru/kupit-komnatu-bez-posrednikov/?deal_type=sale&engine_version=2&is_by_homeowner=1&offer_type=flat&p=1&region=5006&room0=1&sort=creation_date_desc",
            "https://syktyvkar.cian.ru/kupit-zemelniy-uchastok/?deal_type=sale&engine_version=2&object_type%5B0%5D=3&offer_seller_type%5B0%5D=2&offer_type=suburban&p=1&region=5006&sort=creation_date_desc",
            "https://syktyvkar.cian.ru/kupit-dom/?deal_type=sale&engine_version=2&object_type%5B0%5D=1&offer_seller_type%5B0%5D=2&offer_type=suburban&p=1&region=5006&sort=creation_date_desc"
        ]

        cookies = {
            '_CIAN_GK': 'd4d12356-a8ad-405e-aa50-f88ff22ddcae',
            '_gcl_au': '1.1.1838939950.1710491809',
            'login_mro_popup': '1',
            'sopr_utm': '%7B%22utm_source%22%3A+%22yandex%22%2C+%22utm_medium%22%3A+%22organic%22%7D',
            'uxfb_usertype': 'searcher',
            '_ym_uid': '1710491810308334307',
            '_ym_d': '1710491810',
            'uxs_uid': '2abfc210-e2a7-11ee-8471-97b721ddd0bf',
            'session_region_id': '5006',
            'session_main_town_region_id': '5006',
            'cookie_agreement_accepted': '1',
            'newobject_scount': '1',
            'newobject_active': '1',
            'newobject_all': '1',
            'uxfb_card_satisfaction': '%5B299657837%5D',
            '_gid': 'GA1.2.1367976352.1711455718',
            '_ym_isad': '2',
            '__cf_bm': 'zJ0.BFhxrNtnWZ.v3zxkEwoeh1clCDzTzymfYcPIsAY-1711467255-1.0.1.1-nLTWPxZa23QYscmhZTFSXleBiuEm8ysOm3Snprxc.jTGe5UodMg7YaDGV6agt8CvbyUSpjoJOtAoTyi0JrQO2A',
            'sopr_session': 'fc4b040ce5bc4e6d',
            '_ga': 'GA1.2.456011358.1710491810',
            '_ym_visorc': 'b',
            '_ga_3369S417EL': 'GS1.1.1711467254.14.1.1711467828.60.0.0',
        }

        headers = {
            'authority': 'syktyvkar.cian.ru',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            # 'cookie': '_CIAN_GK=d4d12356-a8ad-405e-aa50-f88ff22ddcae; _gcl_au=1.1.1838939950.1710491809; login_mro_popup=1; sopr_utm=%7B%22utm_source%22%3A+%22yandex%22%2C+%22utm_medium%22%3A+%22organic%22%7D; uxfb_usertype=searcher; _ym_uid=1710491810308334307; _ym_d=1710491810; uxs_uid=2abfc210-e2a7-11ee-8471-97b721ddd0bf; session_region_id=5006; session_main_town_region_id=5006; cookie_agreement_accepted=1; newobject_scount=1; newobject_active=1; newobject_all=1; uxfb_card_satisfaction=%5B299657837%5D; _gid=GA1.2.1367976352.1711455718; _ym_isad=2; __cf_bm=zJ0.BFhxrNtnWZ.v3zxkEwoeh1clCDzTzymfYcPIsAY-1711467255-1.0.1.1-nLTWPxZa23QYscmhZTFSXleBiuEm8ysOm3Snprxc.jTGe5UodMg7YaDGV6agt8CvbyUSpjoJOtAoTyi0JrQO2A; sopr_session=fc4b040ce5bc4e6d; _ga=GA1.2.456011358.1710491810; _ym_visorc=b; _ga_3369S417EL=GS1.1.1711467254.14.1.1711467828.60.0.0',
            'sec-ch-ua': '"Not A(Brand";v="99", "Opera GX";v="107", "Chromium";v="121"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0 (Edition Yx GX 03)',
        }

        await ParsingPages(urls_pars, current_panel, class_ads, cookies=cookies, headers=headers).parsing_page()

        # await asyncio.sleep(180)

        # logging.info(f'Возникла ошибка Cian')
        # await asyncio.sleep(60)


if __name__ == '__main__':
    asyncio.run(get_pages_cian())
