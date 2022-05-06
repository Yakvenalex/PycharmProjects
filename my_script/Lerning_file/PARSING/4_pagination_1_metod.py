import requests
from bs4 import BeautifulSoup
import csv

def get_good_price(price):
    price = price.split()
    new_price = []
    if len(price) == 3:
        new_price = price[0] + price[1]
        return new_price
    else:
        return price[0]

def get_html(url):
    r = requests.get(url)
    if r.ok:
        return r.text
    else:
        print(r.status_code)

def write_csv(data):
    with open('tetyana.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'], data['sku'], data['price'], data['link'], data['status']))

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    card = soup.find('ul', class_='cs-product-gallery__list')

    for i in card:
        link = i.find(class_='cs-product-gallery__info-panel').find('a', class_='cs-goods-title').get('href')
        name = i.find(class_='cs-product-gallery__info-panel').find('a', class_='cs-goods-title').text
        price = get_good_price(i.find(class_='cs-product-gallery__info-panel').find(class_='cs-goods-price').text)
        status = i.find(class_='cs-product-gallery__info-panel').\
            find(class_='cs-product-gallery__data cs-goods-data').find('span').text
        sku = i.find(class_='cs-product-gallery__btn-panel').find(class_='cs-product-gallery__sku cs-goods-sku').\
            find('span').get('title')

        data = {'name': name, 'sku': sku, 'price': price, 'link': link, 'status': status}
        write_csv(data)
        print(f'Информация по товару {name} получена и записана!')

def main():
    pattern = 'https://shtory-tanova.com.ua/g13702686-tkan-rogozhka-dlya/page_{}'
    for p in range(1, 6):
        url = pattern.format(str(p))
        get_data(get_html(url))
        print('Парсинг по заданным значениям завершен успешно!')

main()