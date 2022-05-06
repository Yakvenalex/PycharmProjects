import requests
from bs4 import BeautifulSoup
import csv


def get_good_price(price):
    price = price.split()
    new_price = price[0] + price[1]
    return new_price

def get_good_link(link):
    return 'https://modress.ru' + link

def get_html(url):
    r = requests.get(url)
    return r.text

def write_csv(data):
    with open('dress.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'], data['price'], data['link']))

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    products = soup.find('div', id='products').find_all('div', class_='box prod')

    for product in products:
        link = get_good_link(product.find('a').get('href'))
        price = get_good_price(product.find('a').find('span', class_='price').text)
        name = product.find('a').find('span', class_='name').text

        data = {'link': link, 'price': price, 'name': name}
        write_csv(data)

def main():
    url = 'https://modress.ru/catalog/verkhnyaya-odezhda/?PAGEN_1=1'
    print(f'{url} данные получены и записаны успешно!')

    while True:
        get_data(get_html(url))

        soup = BeautifulSoup(get_html(url), 'lxml')
        try:
            url = 'https://modress.ru' + \
                  soup.find('div', class_='pager no-mob').find_all('li')[6].find('a').get('href')
            print(f'{url} данные получены и записаны успешно!')
        except:
            print('Обработка завершена!')
            break

main()