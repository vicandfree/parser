import math

import requests

from context import create_computer


def get_cookies():
    return {
        '__lhash_': '6dae09bf5b21d9c69b7861c7497d89e8',
        'MVID_ACTOR_API_AVAILABILITY': 'true',
        'MVID_BLACK_FRIDAY_ENABLED': 'true',
        'MVID_CART_AVAILABILITY': 'true',
        'MVID_CATALOG_STATE': '1',
        'MVID_CITY_ID': 'CityCZ_9912',
        'MVID_COOKIE': '3500',
        'MVID_CREDIT_AVAILABILITY': 'true',
        'MVID_CRITICAL_GTM_INIT_DELAY': '3000',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GEOLOCATION_NEEDED': 'true',
        'MVID_GIFT_KIT': 'true',
        'MVID_GLC': 'true',
        'MVID_GLP': 'true',
        'MVID_GTM_ENABLED': '011',
        'MVID_IMG_RESIZE': 'true',
        'MVID_INTERVAL_DELIVERY': 'true',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_KLADR_ID': '2200000100000',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_LP_SOLD_VARIANTS': '3',
        'MVID_MCLICK': 'true',
        'MVID_MCLICK_NEW': 'true',
        'MVID_MINDBOX_DYNAMICALLY': 'true',
        'MVID_MINI_PDP': 'true',
        'MVID_NEW_ACCESSORY': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_PROMO_CATALOG_ON': 'true',
        'MVID_REGION_ID': '37',
        'MVID_REGION_SHOP': 'S933',
        'MVID_SERVICES': '111',
        'MVID_TIMEZONE_OFFSET': '7',
        'MVID_WEB_SBP': 'true',
        'SENTRY_ERRORS_RATE': '0.1',
        'SENTRY_TRANSACTIONS_RATE': '0.5',
        '_ym_uid': '1675601587937986044',
        '_ym_d': '1675601587',
        '_ym_isad': '2',
        '_gid': 'GA1.2.663056139.1675601588',
        '_sp_ses.d61c': '*',
        'gdeslon.ru.__arc_domain': 'gdeslon.ru',
        'gdeslon.ru.user_id': '4da0938f-3008-48ef-b2df-03a46da178f8',
        'advcake_track_id': '8a7cbfe9-281f-e800-61f0-4513c0b0266c',
        'advcake_session_id': '3f6732b9-c80b-9b40-8d85-4588071c23c3',
        'tmr_lvid': 'b78bc5db2f327966be948679bc1aff99',
        'tmr_lvidTS': '1675601591083',
        'adrdel': '1',
        'adrcid': 'Am1bG6M5-g8ImwSnMG1wQkg',
        'flocktory-uuid': '032a48e8-3de3-4174-9755-811d1cca316f-1',
        'flacktory': 'no',
        'BIGipServeratg-ps-prod_tcp80': '1141169162.20480.0000',
        'bIPs': '-826759811',
        'afUserId': '6d9d4fb0-d4ec-4163-a1e3-2e87bc708c5a-p',
        'AF_SYNC': '1675601593364',
        'uxs_uid': '0fa76d20-a554-11ed-aac0-cd9733243f3c',
        'mindboxDeviceUUID': '513a868f-644b-44e8-a6e7-c672b70ec18d',
        'directCrm-session': '%7B%22deviceGuid%22%3A%22513a868f-644b-44e8-a6e7-c672b70ec18d%22%7D',
        'cookie_ip_add': '188.133.193.48',
        '_sp_id.d61c': '957aa957-28be-4660-b2fa-b683220fda23.1675601588.1.1675602068..524e09a5-50c9-448c-bfb4-402e732cd099..bd8051a9-5def-4233-895d-ce011d40da5c.1675601587835.44',
        '_ga': 'GA1.2.203513154.1675601587',
        'tmr_detect': '0%7C1675602074008',
        '_ga_CFMZTSS5FM': 'GS1.1.1675601587.1.1.1675602394.0.0.0',
        '_ga_BNX5WPP3YK': 'GS1.1.1675601587.1.1.1675602394.60.0.0',
        'MVID_ENVCLOUD': 'prod1',
    }


def get_header():
    return {
        'authority': 'www.mvideo.ru',
        'accept': 'application/json',
        'accept-language': 'ru,en;q=0.9',
        'baggage': 'sentry-transaction=%2F,sentry-public_key=1e9efdeb57cf4127af3f903ec9db1466,sentry-trace_id=09a5213fa41e405cb2c7e48e6133dd2d,sentry-sample_rate=0.5',
        'referer': 'https://www.mvideo.ru/komputernaya-tehnika-4107/sistemnye-bloki-80/f/tolko-v-nalichii=da?reff=menu_main&sort=price_asc&page=1',
        'sec-ch-ua': '"Chromium";v="106", "Yandex";v="22", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sentry-trace': '09a5213fa41e405cb2c7e48e6133dd2d-895eff57788c2740-0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.3.823 Yowser/2.5 Safari/537.36',
        'x-set-application-id': '3c577e3e-8e8c-4164-b846-01a98796ebb9',
    }


def get_total_count():
    params = {
        'categoryId': '80',
        'offset': '0',
        'limit': '24',
        'sort': 'price_asc',
        'filterParams': 'WyJ0b2xrby12LW5hbGljaGlpIiwiIiwiZGEiXQ==',
        'doTranslit': 'true',
    }
    return requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=get_cookies(),
                               headers=get_header()).json().get('body').get('total')


def get_products_id(offset):
    params = {
        'categoryId': '80',
        'offset': str(offset),
        'limit': 24,
        'sort': 'price_asc',
        'filterParams': 'WyJ0b2xrby12LW5hbGljaGlpIiwiIiwiZGEiXQ==',
        'doTranslit': 'true',
    }

    return requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=get_cookies(),
                        headers=get_header()).json().get('body').get('products')


def get_products_data(products_id):
    json_data = {
        'productIds': products_id,
        'mediaTypes': [
            'images',
        ],
        'category': True,
        'status': True,
        'brand': True,
        'propertyTypes': [
            'KEY',
        ],
        'propertiesConfig': {
            'propertiesPortionSize': 5,
        },
        'multioffer': False,
    }

    return requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=get_cookies(), headers=get_header(),
                         json=json_data).json().get('body').get('products')


def get_products_price(products_id):
    products_ids_str = ','.join(products_id)
    params = {
        'productIds': products_ids_str,
        'addBonusRubles': 'true',
        'isPromoApplied': 'true',
    }

    material_price = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=get_cookies(),
                                  headers=get_header()).json().get('body').get('materialPrices')

    products_price = {}

    for product in material_price:
        product_id = product.get('price').get('productId')
        product_base_price = product.get('price').get('basePrice')

        products_price[product_id] = {
            'basePrice': product_base_price
        }

    return products_price


def get_cpu_hhz(properties):
    for p in properties:
        if p['name'] == 'Тип процессора':
            value = p['value']
            value = value.split('ГГц')[0].split(' ')[-2]
            return float(value)


def get_ram_gb(properties):
    for p in properties:
        if p['name'] == 'Оперативная память (RAM)':
            return int(p['value'])


def get_ssd_gb(properties):
    for p in properties:
        if p['name'] == 'Объем SSD':
            value = p['value']
            return int(value.split(' ')[0])
    return 0

async def insert_in_db(products_data, products_price, session_maker):
    for p in products_data:
        await create_computer(
            url=f'https://www.mvideo.ru/products/{p["nameTranslit"]}-{p["productId"]}',
            name=p['name'],
            cpu_hhz=get_cpu_hhz(p['propertiesPortion']),
            ram_gb=get_ram_gb(p['propertiesPortion']),
            ssd_gb=get_ssd_gb(p['propertiesPortion']),
            price=products_price[p["productId"]]['basePrice'],
            session_maker=session_maker)


async def parse_mvideo(session_maker):
    total_count = get_total_count()
    pages_count = math.ceil(total_count / 24)
    for i in range(0, pages_count):
        products_id = get_products_id(i * 24)
        products_data = get_products_data(products_id)
        products_price = get_products_price(products_id)
        await insert_in_db(products_data, products_price, session_maker)
