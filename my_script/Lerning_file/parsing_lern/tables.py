import requests
from bs4 import BeautifulSoup
import csv

def get_html(url):
    r = requests.get(url)
    return r.text

def write_csv(data):
    with open('cmcc.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([data['name'],
                         data['link'],
                         data['price']])

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    trs = soup.find('table', class_='h7vnx2-2 czTsgW cmc-table').find('tbody').find_all('tr')

    for tr in trs:
        tds = tr.find_all('td')
        link = tds[2].find('a').get('href')
        link = 'https://coinmarketcap.com'+link
        name = tds[2].find('a').find('img')
        price = tds[3].find('a')

        try:
            price = tds[3].find('span').text
        except:
            price = tds[3].find('a').find('span').text

        try:
            name = tds[2].find_all('span')[1].text
        except:
            name = tds[2].find('a').find('p').text

        price = price[1:]
        if ',' in price:
            price = price.replace(',', '')

        data = {'name': name,
                'link': link,
                'price': price}

        write_csv(data)

def main():
    url = 'https://coinmarketcap.com/'
    get_page_data( get_html(url) )
    print('Парсинг завершен')

if __name__ == '__main__':
    main()