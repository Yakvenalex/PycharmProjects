from multiprocessing import Pool
import requests
from bs4 import BeautifulSoup

print('Начинаю сканирование страниц для поиска ссылок на объявления...')
print('Стартовал! Результат будет через минутку 😉')

l = []
pattern = 'https://gde.ru/tovari_dlya_detei?page={}'

def get_list_link():

    for u in range(1, 11):
        url = pattern.format(str(u))
        r = requests.get(url).text
        soup = BeautifulSoup(r, 'lxml')
        block = soup.find_all('div', class_='info-content')

        for i in block:
            link = i.find('a').get('href')
            l.append(link)
    return l
my_link_list = get_list_link()

print(f'Я отсканироал тебе 10 страниц и нашел {len(my_link_list)} сылок на объявления')
print('Приступаю к парсингу номеров по объявлениям')