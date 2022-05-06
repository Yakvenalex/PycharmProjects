import requests
from bs4 import BeautifulSoup
import csv

def get_html(url):
    r = requests.get(url)
    return r.text

def refind(s):
    # из полученных строк сделал список и в каждом вывел первое значение [0]
    rai = s.split(' ')[0]
    # заменил запятую на отсутствие пробела (удалил запятую в цифре)
    return rai.replace(',', '')

def wite_csv_n():
    data_0 = ['Название плагина', "Ссылка на плагин", 'Рейтинг плагина']
    with open('plugins.csv', 'w', newline='') as f:
        writer = csv.writer(f)

        writer.writerow([data_0[0], data_0[1], data_0[2]])
wite_csv_n()

def wite_csv(data):
    # newline='' - пришлось добавить чтоб не появлялась пустая строка!
    with open('plugins.csv', 'a', newline='') as f:
        writer = csv.writer(f)

        list_data = [data['name'], data['url'],  data['reviews']]
        writer.writerow(list_data)

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    popular = soup.find_all('section')[3]
    plugins = popular.find_all('article')

    for plugin in plugins:
        name = plugin.find('h3').text
        url = plugin.find('h3').find('a').get('href')
        rating_0 = plugin.find('span', class_='rating-count').find('a').text
        rating = refind(rating_0)

        data = {'name': name,
                'url': url,
                'reviews' : rating}
        wite_csv(data)


def main():
    url = 'https://wordpress.org/plugins/'
    get_data(get_html(url))
    print('Добавление информации в CSV. Статус ==> УСПЕХ!')

if __name__ == '__main__':
    main()