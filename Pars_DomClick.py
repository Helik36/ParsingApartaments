import asyncio
import os
import logging
import re
import time

import requests

from bs4 import BeautifulSoup

from check_in_db import append_urls, check_url_in_db, append_new_url_from_pars

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
                'ns_session': '3085b49b-8790-4b56-9193-cc32a0a73a8e',
                'ftgl_cookie_id': 'c71521422eb91873cb826aa247659428',
                'RETENTION_COOKIES_NAME': '129128f494834cf38c8afe806bf3f901:zEkIcSSADnNMEsIwtikk6hOdrzY',
                'sessionId': '7804095f33164b0c871dc960b9d7a6aa:ZE2xiU749cm5SSgOA4q0WpVcO_0',
                'UNIQ_SESSION_ID': '5d63f584701b44e4a8665d8fef1eb965:yjbdnKB6Ul1YvCp-ovFwoe48WAA',
                'rent-experiment': 'false',
                '_ym_uid': '1710492189839526613',
                '_ym_d': '1710492189',
                'logoSuffix': '',
                '_gcl_au': '1.1.363831076.1710492189',
                'region': '{%22data%22:{%22name%22:%22%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%22%2C%22kladr%22:%2277%22%2C%22guid%22:%221d1463ae-c80f-4d19-9331-a1b68a85b553%22}%2C%22isAutoResolved%22:true}',
                '_ga': 'GA1.1.1042123187.1710492190',
                'tmr_lvid': 'a77b9386f565857f1926f49e842996dc',
                'tmr_lvidTS': '1710492189683',
                'regionAlert': '1',
                'auto-definition-region': 'false',
                'currentLocalityGuid': '84ebe7b3-7313-4a81-aaa5-415c5cf497af',
                'currentRegionGuid': '3002967f-837e-4a5b-9d95-c9520cad9f74',
                'currentSubDomain': 'syktyvkar',
                'regionName': '84ebe7b3-7313-4a81-aaa5-415c5cf497af:%D0%A1%D1%8B%D0%BA%D1%82%D1%8B%D0%B2%D0%BA%D0%B0%D1%80',
                '___dmpkit___': 'c1a104a7-f3c1-4fa6-ab01-942b53289f5b',
                'dtCookie': 'v_4_srv_6_sn_273EF5DB673E05388970EB112C15F29C_perc_100000_ol_0_mul_1_app-3Aca312da39d5a5d07_1_app-3A6ea6d147da1fb68a_1_rcs-3Acss_0',
                'rxVisitor': '1710492274109VNQMJMUQKJBH8CHALOAHNG5UPUSFEN3O',
                'cookieAlert': '1',
                'dtSa': '-',
                'rxvt': '1710859250623|1710857332471',
                'dtPC': '6$257450128_447h-vBDKJUIMKUIPPMPGMOCOMOWNVQJAAMNDV-0e0',
                '_ym_isad': '2',
                'qrator_ssid': '1711053180.044.kZxVb4p9R6U35Wcw-qnov9hdn9ujgvjrlsibkhac0mmu4l86n',
                'qrator_jsid': '1711053179.230.3XT91kIHlU9iaMeS-rmravabuqk6ilglfq6i65spauus6lnfc',
                '_visitId': '553403c8-b32a-4b28-bfa0-86ec02f6e4b4-f2e0a38fc064752a',
                'tmr_detect': '1%7C1711055146628',
                '_ga_NP4EQL89WF': 'GS1.1.1711055146.9.1.1711055547.60.0.0',
                'tmr_reqNum': '123',
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