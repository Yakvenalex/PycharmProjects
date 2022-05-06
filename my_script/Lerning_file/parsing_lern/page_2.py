import requests
from bs4 import BeautifulSoup
import csv
import re

def get_good_link(l):
    x = 'https://coinmarketcap.com'
    return x + str(l)

def get_good_price(p):
    p = p[1:]

    if ',' in p:
        p = p.replace(',', '')
    return p

def get_html(url):
    r = requests.get(url)
    if r.ok:
        return r.text
    else:
        print(r.status_code)

def write_csv(data):
    with open('crypta.csv', 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'],
                         data['price'],
                         data['link']))

#  data = {'name': name, 'price': price, 'link': link}
def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    trs = soup.find('table', class_='h7vnx2-2 czTsgW cmc-table').find('tbody')

    for tr in trs:
        try:
            name = tr.find('div', class_='sc-16r8icm-0 escjiH').find('p').text
        except:
            name= tr.find_all('span')[3].text

        try:
            link = get_good_link(tr.find('div', class_='sc-16r8icm-0 escjiH').find('a').get('href'))
        except:
            link = get_good_link(tr.find('a').get('href'))

        try:
            price = get_good_price(tr.find('div', class_='sc-131di3y-0 cLgOOr').find('span').text)
        except:
            price = get_good_price(tr.find_all('span')[5].text)

        data = {'name': name, 'price': price, 'link': link}

        write_csv(data)

def main():
    url = 'https://coinmarketcap.com/'

    while True:
        get_page_data(get_html(url))
        soup = BeautifulSoup(get_html(url), 'lxml')

        print(f'Данные со страницы {url} - записаны!')

        try:
            url = get_good_link(soup.find('li',class_='next').find('a').get('href'))
        except:
            break
    main()

if __name__ == '__main__':
    main()