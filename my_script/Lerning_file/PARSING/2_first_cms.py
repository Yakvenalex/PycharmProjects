import requests
from bs4 import BeautifulSoup
import csv

def good_count(count):
    result = count.split()[0]
    return result.replace(',', '')

def get_html(url):
    r = requests.get(url)
    return r.text

def write_csv(data):
    with open('pl.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'], data['count'], data['link']))

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    popular = soup.find_all('section')[3].find_all('article')

    for i in popular:
        link = i.find('a').get('href')
        name = i.find('h3').text
        count = good_count(i.find('span', class_='rating-count').find('a').text)
        data = {'name': name, 'count': count, 'link': link}

        write_csv(data)

def main():
    url = 'https://wordpress.org/plugins/'
    get_data(get_html(url))
    print('Процесс записи успешно завершен!')

if __name__ == '__main__':
    main()