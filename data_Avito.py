import asyncio
import logging

from Parsing import ParsingSites

logging.basicConfig(
    format="[%(asctime)s]: %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
    level=logging.INFO)

current_panel = "items-items-kAJAg"
class_ads = "iva-item-sliderLink-uLz1v"


async def pars_html_avito():
    urls_pars = ["https://www.avito.ru/syktyvkar/kvartiry/prodam-ASgBAgICAUSSA8YQ?f=ASgBAgICAkSSA8YQkL4Nlq41&s=104",
                 "https://www.avito.ru/syktyvkar/doma_dachi_kottedzhi/prodam-ASgBAgICAUSUA9AQ?cd=1&p=1&s=104&user=1",
                 "https://www.avito.ru/syktyvkar/komnaty/prodam-ASgBAgICAUSQA7wQ?cd=1&localPriority=1&s=104&user=1",
                 "https://www.avito.ru/syktyvkar/zemelnye_uchastki/prodam-ASgBAgICAUSWA9oQ?cd=1&s=104&user=1"]

    cookies = {
        'srv_id': 'FHt9AAx7oEzDiOo5.PFI3AEDMPnyUBrisRKKJ2qjm9uQrWKvpGK9aIEC8OpxhFVzSHdRMgWb3U1LH180=.t1JLP2_MEjpJOeUODaJ-MeQ9cPDE7J5t7x72zmzJMqU=.web',
        'u': '32e828rd.q4q4vk.10azkslkgpvg0',
        '_gcl_au': '1.1.273815383.1709729418',
        '_ga': 'GA1.1.665494094.1709729419',
        'uxs_uid': '167b5170-dbb8-11ee-861c-19f1128e5be6',
        '_ym_uid': '1709729420243526045',
        '_ym_d': '1709729420',
        'SEARCH_HISTORY_IDS': '1',
        'buyer_laas_location': '648630',
        'yandex_monthly_cookie': 'true',
        '__zzatw-avito': 'MDA0dBA=Fz2+aQ==',
        '__zzatw-avito': 'MDA0dBA=Fz2+aQ==',
        'cfidsw-avito': 'NXZtzpVxQmhA+OtMVrltw1SFtdGUGMJ6O98mLfEtdc7tby9NXgboyQOdSnn2qYjRspH38XVo3+CY/DpYIg6R5B61PSaklBMhO4qW/vfk4mc1s0BzKSPjwWL7t+Vcsu8/RnzsEbllt9zf/jaYRqakU+xdS/fhfypFVNJI',
        'cfidsw-avito': 'NXZtzpVxQmhA+OtMVrltw1SFtdGUGMJ6O98mLfEtdc7tby9NXgboyQOdSnn2qYjRspH38XVo3+CY/DpYIg6R5B61PSaklBMhO4qW/vfk4mc1s0BzKSPjwWL7t+Vcsu8/RnzsEbllt9zf/jaYRqakU+xdS/fhfypFVNJI',
        'cfidsw-avito': 'HqqOFiw4IBULsBtsRS4rVK65bF3oX8wnBgBv/x9hz/FxmOWgABDFoA5y5F7zrQr7R636+5A+r/oqi1nmREpgp6bqAuPTJ096I2GB2W3Qx22R7EfRpxAmEukp588sMjSsYmFPwgGVn76VvFgXHDwI1nha/8xdBP8HyJFm',
        'sessid': '34a138e468cf3bfc37980aa33ff53cc1.1709731027',
        'auth': '1',
        'tmr_lvid': 'd2780274f30f262245a763240adcdb14',
        'tmr_lvidTS': '1709931136436',
        'view': 'default',
        'buyer_location_id': '648630',
        'abp': '0',
        '_ga_ZJDLBTV49B': 'GS1.1.1710147378.20.0.1710147378.0.0.0',
        '_ga_WW6Q1STJ8M': 'GS1.1.1710147378.20.0.1710147378.0.0.0',
        'v': '1711455245',
        'luri': 'syktyvkar',
        'sx': 'H4sIAAAAAAAC%2FwTAQRLCIAwF0Lv8tQtDg0m4DWCidVEZ7XRhh7v7Tmhkdrm6cbpXX1IjE4%2Fem3mtIQ3lxIGC%2Fj1%2BC%2FErxpPG2DXpW21dH7btm8QHFzgKCVFmunGe8x8AAP%2F%2FsbLQbFsAAAA%3D',
        'dfp_group': '69',
        'isLegalPerson': '0',
        '_ga_M29JC28873': 'GS1.1.1711455246.36.0.1711455246.60.0.0',
        'gMltIuegZN2COuSe': 'EOFGWsm50bhh17prLqaIgdir1V0kgrvN',
        'f': '5.9683c10f450c271efe85757b7948761ec1e8912fd5a48d02c1e8912fd5a48d02c1e8912fd5a48d02c1e8912fd5a48d02c1e8912fd5a48d02c1e8912fd5a48d02c1e8912fd5a48d02c1e8912fd5a48d02c1e8912fd5a48d02c1e8912fd5a48d0246b8ae4e81acb9fa1a2a574992f83a9246b8ae4e81acb9fa46b8ae4e81acb9fae992ad2cc54b8aa8068fd850112c943dbcc8809df8ce07f640e3fb81381f359178ba5f931b08c66a59b49948619279110df103df0c26013a2ebf3cb6fd35a0acf722fe85c94f7d0c0df103df0c26013a7b0d53c7afc06d0bba0ac8037e2b74f92da10fb74cac1eab71e7cb57bbcb8e0f71e7cb57bbcb8e0f2da10fb74cac1eab0df103df0c26013a037e1fbb3ea05095de87ad3b397f946b4c41e97fe93686ad65e98d685f52b20160a59c80bd86909602c730c0109b9fbbbed46eb817dfcec071495e195e0d4725aff5a88f928bb65fcccf34479686bada8db57d0f7c7638d40df103df0c26013a0df103df0c26013aafbc9dcfc006bed9938a45572a3e5b056028f49e254905b03de19da9ed218fe23de19da9ed218fe2dc4f5790d1ff098f2fd5948f5c676efa78a492ecab7d2b7f',
        'ft': '"hFi4cWqdYgKpItuPlBF1HgIkFJv6c4BsvSccevOPnYqG5Y9eKRVbZcztXshmniaBQP/FcRP65WahZLCaiKqpeqfiQIvA+U2mn97a14wA5sZVFw2JVwTgymyWanWD+0cBHkOnUBNID/1MyOnCq2Usti2jyTBPxn6lKu8dCuvwd4Hqtivbsciy2vdTVer5wOjr"',
        '_ym_isad': '2',
        'cartCounter': '0',
        '_ym_visorc': 'b',
        'buyer_from_page': 'catalog',
    }

    headers = {
        'authority': 'www.avito.ru',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        # 'cookie': 'srv_id=FHt9AAx7oEzDiOo5.PFI3AEDMPnyUBrisRKKJ2qjm9uQrWKvpGK9aIEC8OpxhFVzSHdRMgWb3U1LH180=.t1JLP2_MEjpJOeUODaJ-MeQ9cPDE7J5t7x72zmzJMqU=.web; u=32e828rd.q4q4vk.10azkslkgpvg0; _gcl_au=1.1.273815383.1709729418; _ga=GA1.1.665494094.1709729419; uxs_uid=167b5170-dbb8-11ee-861c-19f1128e5be6; _ym_uid=1709729420243526045; _ym_d=1709729420; SEARCH_HISTORY_IDS=1; buyer_laas_location=648630; yandex_monthly_cookie=true; __zzatw-avito=MDA0dBA=Fz2+aQ==; __zzatw-avito=MDA0dBA=Fz2+aQ==; cfidsw-avito=NXZtzpVxQmhA+OtMVrltw1SFtdGUGMJ6O98mLfEtdc7tby9NXgboyQOdSnn2qYjRspH38XVo3+CY/DpYIg6R5B61PSaklBMhO4qW/vfk4mc1s0BzKSPjwWL7t+Vcsu8/RnzsEbllt9zf/jaYRqakU+xdS/fhfypFVNJI; cfidsw-avito=NXZtzpVxQmhA+OtMVrltw1SFtdGUGMJ6O98mLfEtdc7tby9NXgboyQOdSnn2qYjRspH38XVo3+CY/DpYIg6R5B61PSaklBMhO4qW/vfk4mc1s0BzKSPjwWL7t+Vcsu8/RnzsEbllt9zf/jaYRqakU+xdS/fhfypFVNJI; cfidsw-avito=HqqOFiw4IBULsBtsRS4rVK65bF3oX8wnBgBv/x9hz/FxmOWgABDFoA5y5F7zrQr7R636+5A+r/oqi1nmREpgp6bqAuPTJ096I2GB2W3Qx22R7EfRpxAmEukp588sMjSsYmFPwgGVn76VvFgXHDwI1nha/8xdBP8HyJFm; sessid=34a138e468cf3bfc37980aa33ff53cc1.1709731027; auth=1; tmr_lvid=d2780274f30f262245a763240adcdb14; tmr_lvidTS=1709931136436; view=default; buyer_location_id=648630; abp=0; _ga_ZJDLBTV49B=GS1.1.1710147378.20.0.1710147378.0.0.0; _ga_WW6Q1STJ8M=GS1.1.1710147378.20.0.1710147378.0.0.0; v=1711455245; luri=syktyvkar; sx=H4sIAAAAAAAC%2FwTAQRLCIAwF0Lv8tQtDg0m4DWCidVEZ7XRhh7v7Tmhkdrm6cbpXX1IjE4%2Fem3mtIQ3lxIGC%2Fj1%2BC%2FErxpPG2DXpW21dH7btm8QHFzgKCVFmunGe8x8AAP%2F%2FsbLQbFsAAAA%3D; dfp_group=69; isLegalPerson=0; _ga_M29JC28873=GS1.1.1711455246.36.0.1711455246.60.0.0; gMltIuegZN2COuSe=EOFGWsm50bhh17prLqaIgdir1V0kgrvN; f=5.9683c10f450c271efe85757b7948761ec1e8912fd5a48d02c1e8912fd5a48d02c1e8912fd5a48d02c1e8912fd5a48d02c1e8912fd5a48d02c1e8912fd5a48d02c1e8912fd5a48d02c1e8912fd5a48d02c1e8912fd5a48d02c1e8912fd5a48d0246b8ae4e81acb9fa1a2a574992f83a9246b8ae4e81acb9fa46b8ae4e81acb9fae992ad2cc54b8aa8068fd850112c943dbcc8809df8ce07f640e3fb81381f359178ba5f931b08c66a59b49948619279110df103df0c26013a2ebf3cb6fd35a0acf722fe85c94f7d0c0df103df0c26013a7b0d53c7afc06d0bba0ac8037e2b74f92da10fb74cac1eab71e7cb57bbcb8e0f71e7cb57bbcb8e0f2da10fb74cac1eab0df103df0c26013a037e1fbb3ea05095de87ad3b397f946b4c41e97fe93686ad65e98d685f52b20160a59c80bd86909602c730c0109b9fbbbed46eb817dfcec071495e195e0d4725aff5a88f928bb65fcccf34479686bada8db57d0f7c7638d40df103df0c26013a0df103df0c26013aafbc9dcfc006bed9938a45572a3e5b056028f49e254905b03de19da9ed218fe23de19da9ed218fe2dc4f5790d1ff098f2fd5948f5c676efa78a492ecab7d2b7f; ft="hFi4cWqdYgKpItuPlBF1HgIkFJv6c4BsvSccevOPnYqG5Y9eKRVbZcztXshmniaBQP/FcRP65WahZLCaiKqpeqfiQIvA+U2mn97a14wA5sZVFw2JVwTgymyWanWD+0cBHkOnUBNID/1MyOnCq2Usti2jyTBPxn6lKu8dCuvwd4Hqtivbsciy2vdTVer5wOjr"; _ym_isad=2; cartCounter=0; _ym_visorc=b; buyer_from_page=catalog',
        'sec-ch-ua': '"Not A(Brand";v="99", "Opera GX";v="107", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0 (Edition Yx GX 03)',
    }

    while True:

        try:
            await ParsingSites(urls_pars, current_panel, class_ads, cookies=cookies, headers=headers).parsing_page()
            await asyncio.sleep(180)

        except:
            logging.info(f'Возникла ошибка Avito')
            await asyncio.sleep(45)


if __name__ == '__main__':
    asyncio.run(pars_html_avito())
