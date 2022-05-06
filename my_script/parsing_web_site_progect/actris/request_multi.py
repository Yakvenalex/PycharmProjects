from multiprocessing import Pool
import requests
from bs4 import BeautifulSoup
import csv

def get_html(url):
    r = requests.get(url)
    if r.ok:
        return r.text
    else:
        print(r.status_code)

def write_csv(data):
    with open('3y.csv', 'a', newline='', encoding="utf-8") as f:
        order = ['name', 'age', 'like', 'link']
        writer = csv.DictWriter(f, fieldnames=order)
        writer.writerow(data)

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    block = soup.find_all('div', class_='iso_grid-5-item_full')
    for i in block:
        try:
            name = i.find('h4').text
        except:
            name = 'none'
        try:
            link = 'https://ruskino.ru' + i.find('a').get('href')
        except:
            link = 'none'
        try:
            age = i.find_all('span')[0].text.strip().split()[0]
        except:
            age = 'none'
        try:
            like = i.find_all('span')[1].text.strip().split()[0]
        except:
            like = 'none'
        data = {'name': name, 'link': link, 'age': age, 'like': like}
        write_csv(data)

def make_all(url):
    html = get_html(url)
    get_data(html)

def main():
    url = 'https://ruskino.ru/art/groups/actresses?page={}'
    my_list = [url.format(str(i)) for i in range(1, 11)]

    with Pool(2) as p:
        p.map(make_all, my_list)

if __name__ == '__main__':
    main()