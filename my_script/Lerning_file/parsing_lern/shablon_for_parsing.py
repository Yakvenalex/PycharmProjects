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
    with open('name_file.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        pass

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    block = soup.find_all('div')

def main():
    url = 'https://site.ru'
    # get_page_data( get_html(url) )
    pass

if __name__ == '__main__':
    main()