import asyncio
import logging
from Parsing import ParsingSites

logging.basicConfig(
    format="[%(asctime)s]: %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
    level=logging.INFO)

current_panel = "_93444fe79c--wrapper--W0WqH"
class_ads = "_93444fe79c--link--VtWj6"


async def pars_html_cian():
    urls_pars = [
        "https://syktyvkar.cian.ru/kupit-kvartiru/?deal_type=sale&engine_version=2&offer_seller_type%5B0%5D=2&offer_type=flat&p=1&region=5006&room1=1&room2=1&room3=1&room4=1&room5=1&room6=1&sort=creation_date_desc",
        "https://syktyvkar.cian.ru/kupit-komnatu-bez-posrednikov/?deal_type=sale&engine_version=2&is_by_homeowner=1&offer_type=flat&p=1&region=5006&room0=1&sort=creation_date_desc",
        "https://syktyvkar.cian.ru/kupit-zemelniy-uchastok/?deal_type=sale&engine_version=2&object_type%5B0%5D=3&offer_seller_type%5B0%5D=2&offer_type=suburban&p=1&region=5006&sort=creation_date_desc",
        "https://syktyvkar.cian.ru/kupit-dom/?deal_type=sale&engine_version=2&object_type%5B0%5D=1&offer_seller_type%5B0%5D=2&offer_type=suburban&p=1&region=5006&sort=creation_date_desc"
    ]

    cookies = {
        '_CIAN_GK': '24328553-ffc2-4933-b629-8d1e60857be1',
        'uxfb_usertype': 'searcher',
        '_ym_uid': '1698353130935138528',
        '_ym_d': '1698353130',
        'uxs_uid': '998763e0-7440-11ee-8377-1f63c7a816fe',
        'cookie_agreement_accepted': '1',
        '_gcl_au': '1.1.395516783.1710522545',
        'tmr_lvid': '719730b57fe5e02a44e36676ec477922',
        'tmr_lvidTS': '1710522545817',
        'login_mro_popup': '1',
        'adrcid': 'ARDSUskjaUEveJirWjy-R5A',
        'afUserId': 'cac2bd07-890c-469a-9999-869a550d2863-p',
        'session_region_id': '5006',
        'session_main_town_region_id': '5006',
        '_ga_L109H0KCP9': 'GS1.1.1711993582.1.0.1711993592.0.0.0',
        'sopr_utm': '%7B%22utm_source%22%3A+%22google%22%2C+%22utm_medium%22%3A+%22organic%22%7D',
        'adrcid': 'ARDSUskjaUEveJirWjy-R5A',
        'domain_sid': 'OtvXQu64FmDheQwBzl6sO%3A1712661203432',
        '_gid': 'GA1.2.100736729.1712666622',
        '_ym_isad': '2',
        'AF_SYNC': '1712666622754',
        'adrdel': '1',
        '__cf_bm': '2kNxDw4DZ.7c01576xey46xbFF1I4rQaa7YDJtSmat4-1712683539-1.0.1.1-LVV0WCfaGdyq19YSAmIE.XE1AEOwbtExbV0Qv35kJ0ZMhP5hpjKK4NRxOlIQsOtr3GB7s.snkxHLfPGseotriA',
        '__ddg1_': 'PPmHVdwbS7iq8tr9iL5r',
        '_ym_visorc': 'b',
        'sopr_session': '4b38a640ac65405e',
        '_ga': 'GA1.2.1807339557.1698353129',
        'tmr_detect': '0%7C1712683975506',
        '_ga_3369S417EL': 'GS1.1.1712683540.26.1.1712684942.60.0.0',
    }

    headers = {
        'authority': 'syktyvkar.cian.ru',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        # 'cookie': '_CIAN_GK=24328553-ffc2-4933-b629-8d1e60857be1; uxfb_usertype=searcher; _ym_uid=1698353130935138528; _ym_d=1698353130; uxs_uid=998763e0-7440-11ee-8377-1f63c7a816fe; cookie_agreement_accepted=1; _gcl_au=1.1.395516783.1710522545; tmr_lvid=719730b57fe5e02a44e36676ec477922; tmr_lvidTS=1710522545817; login_mro_popup=1; adrcid=ARDSUskjaUEveJirWjy-R5A; afUserId=cac2bd07-890c-469a-9999-869a550d2863-p; session_region_id=5006; session_main_town_region_id=5006; _ga_L109H0KCP9=GS1.1.1711993582.1.0.1711993592.0.0.0; sopr_utm=%7B%22utm_source%22%3A+%22google%22%2C+%22utm_medium%22%3A+%22organic%22%7D; adrcid=ARDSUskjaUEveJirWjy-R5A; domain_sid=OtvXQu64FmDheQwBzl6sO%3A1712661203432; _gid=GA1.2.100736729.1712666622; _ym_isad=2; AF_SYNC=1712666622754; adrdel=1; __cf_bm=2kNxDw4DZ.7c01576xey46xbFF1I4rQaa7YDJtSmat4-1712683539-1.0.1.1-LVV0WCfaGdyq19YSAmIE.XE1AEOwbtExbV0Qv35kJ0ZMhP5hpjKK4NRxOlIQsOtr3GB7s.snkxHLfPGseotriA; __ddg1_=PPmHVdwbS7iq8tr9iL5r; _ym_visorc=b; sopr_session=4b38a640ac65405e; _ga=GA1.2.1807339557.1698353129; tmr_detect=0%7C1712683975506; _ga_3369S417EL=GS1.1.1712683540.26.1.1712684942.60.0.0',
        'sec-ch-ua': '"Not A(Brand";v="99", "Opera GX";v="107", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0',
    }

    prox = "69.197.135.42:18080"

    proxies = {
        'http': prox,
        'https': prox
    }

    while True:
        try:
            await ParsingSites(urls_pars, current_panel, class_ads, cookies=cookies, headers=headers).parsing_page(proxies)
            await asyncio.sleep(180)
        except:
            await asyncio.sleep(45)


if __name__ == '__main__':
    asyncio.run(pars_html_cian())
