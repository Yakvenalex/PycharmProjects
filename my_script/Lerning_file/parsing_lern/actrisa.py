import requests
from bs4 import BeautifulSoup
import csv

def rena(z):
    z = z.split(' ')
    return z

def good_l(l):
    l = 'https://ruskino.ru' + l
    return l

def good_age(a):
    a = a.split(' ')[0]
    return a

def get_html(url):
    r = requests.get(url)
    if r.ok:
        return r.text
    else:
        print(r.status_code)

def write_csv(data):
    with open('actors.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'],
                         data['sur'],
                         data['age'],
                         data['rating'],
                         data['link']))

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    all = soup.find_all('div', class_='iso_item_point')

    for i in all:
        name_all = i.find('h4').text
        link = good_l(i.find('a').get('href'))
        name = rena(name_all)[1]
        sur = rena(name_all)[0]

        try:
            count = i.find('span', class_="main_vote_count").text.strip()
        except:
            count = 'нет данных'

        try:
            age = good_age(i.find('span', class_="main_age_in_list").text.strip())
        except:
            age = 'нет данных'

        data = {'name': name, 'sur': sur, 'age': age, 'rating': count, 'link': link }

        write_csv(data)

def main():
    pattern = 'https://ruskino.ru/art/groups/actresses?page={}'

    for i in range(1, 6):
        url = pattern.format(str(i))
        get_page_data(get_html(url))

        print(f'Страница {url} - успех!')

if __name__ == '__main__':
    main()