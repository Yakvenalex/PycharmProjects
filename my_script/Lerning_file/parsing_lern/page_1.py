import requests
from bs4 import BeautifulSoup
import csv

def get_html(url):
    r = requests.get(url)
    if r.ok:
        return r.text
    print(r.status_code)

def write_csv(data):
    with open('yaca.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'],
                         data['url'],
                         data['text'],
                         data['TIC']))

def give_n(s):
    return s.split(' ')[-1]

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    lis = soup.find_all('li', class_='yaca-snippet')

    for li in lis:
        try:
            name = li.find('h2').text.strip()
        except:
            name = 'Нет данных'

        try:
            link = li.find('h2').find('a').get('href')
        except:
            link = 'Нет данных'

        try:
            desc = li.find('div', class_='yaca-snippet__text').text.strip()
        except:
            desc = 'Нет данных'

        try:
            tic = give_n(li.find('div', class_='yaca-snippet__cy').text)
        except:
            tic = ''

        data = {'name': name, 'url': link, 'text': desc, 'TIC': tic}

        write_csv(data)

def main():
    pattern = 'https://yacca.ru/cat/Entertainment/{}.html'

    for i in range(1, 6):
        url = pattern.format(str(i))
        get_page_data(get_html(url))

        print(f'Информация со страницы: {url} получена и записана!')

if __name__ == '__main__':
    main()