import requests
from bs4 import BeautifulSoup
import csv

def get_right_link(link):
    return 'https://coinmarketcap.com' + link

def get_right_price(price):
    # $415.19
    price = price[1:]

    if ',' in price:
        price = price.replace(',', '')
        return price
    else:
        return price

def get_html(url):
    r = requests.get(url)
    return r.text

def write_csv(data):
    with open('pl.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'], data['price'], data['link']))

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    trs = soup.find('table').find('tbody').find_all('tr')
    for tr in trs:
        link = get_right_link(tr.find_all('td')[2].find('a').get('href'))
        name = tr.find_all('td')[2].find('a')
        price = get_right_price(tr.find_all('td')[3].find('span').text)

        try:
            name = tr.find_all('td')[2].find('a').find('p').text
        except:
            name = tr.find_all('td')[2].find('a').find_all('span')[1].text

        data ={'name': name, 'price': price, 'link': link}

        write_csv(data)

def main():
    url = 'https://coinmarketcap.com/'
    get_data(get_html(url))

main()