import math

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from context import create_computer


async def parse_pc(session_maker):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    driver.get('https://www.dns-shop.ru/catalog/17a8932c16404e77/personalnye-kompyutery/')
    total_count = driver.find_element(By.CLASS_NAME, 'products-count').text.split(' ')[0]
    pages_count = math.ceil(int(total_count) / 18)

    for page in range(1, pages_count):
        driver.get(f'https://www.dns-shop.ru/catalog/17a8932c16404e77/personalnye-kompyutery/?p={page}')
        products = driver.find_elements(By.CLASS_NAME, 'catalog-product')
        products_prices = driver.find_elements(By.CLASS_NAME, 'product-buy__price')
        products_urls = driver.find_elements(By.CLASS_NAME, 'catalog-product__name')
        for i in range(0, len(products)):
            try:
                await create_computer(
                    url=products_urls[i].get_attribute('href'),
                    name=products[i].text.split('[')[0],
                    cpu_hhz=float(products[i].text.split('[')[1].split('x')[1].split(' ГГц')[0]),
                    ram_gb=int(products[i].text.split(' ГБ')[0].split(', ')[-1]),
                    ssd_gb=int(products[i].text.split('SSD ')[1].split(' ГБ')[0]),
                    price=int(products_prices[i].text.split(' ₽')[0].replace(" ", "")),
                    session_maker=session_maker)

            except Exception as _ex:
                ...

    driver.close()
    driver.quit()


async def parse_laptop(session_maker):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    driver.get('https://www.dns-shop.ru/catalog/17a892f816404e77/noutbuki/')
    total_count = driver.find_element(By.CLASS_NAME, 'products-count').text.split(' ')[0]
    pages_count = math.ceil(int(total_count) / 18)

    for page in range(1, pages_count):
        driver.get(f'https://www.dns-shop.ru/catalog/17a892f816404e77/noutbuki/?p={page}')
        products = driver.find_elements(By.CLASS_NAME, 'catalog-product')
        products_prices = driver.find_elements(By.CLASS_NAME, 'product-buy__price')
        products_urls = driver.find_elements(By.CLASS_NAME, 'catalog-product__name')
        for i in range(0, len(products)):
            try:
                await create_computer(
                    url=products_urls[i].get_attribute('href'),
                    name=products[i].text.split('[')[0],
                    cpu_hhz=float(products[i].text.split(' ГГц')[0].split('х ')[1]),
                    ram_gb = int(products[i].text.split(' ГБ')[0].split('RAM ')[-1]),
                    ssd_gb=int(products[i].text.split('SSD ')[1].split(' ГБ')[0]),
                    price=int(products_prices[i].text.split(' ₽')[0].replace(" ", "")),
                    session_maker=session_maker)

            except Exception as _ex:
                ...

    driver.close()
    driver.quit()


async def parse_dns(session_maker):
    await parse_laptop(session_maker)
    await parse_pc(session_maker)
