import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.132 YaBrowser/22.3.1.895 Yowser/2.5 Safari/537.36'}
    r = requests.get(url, headers=user_agent)
    return r.text

def write_csv(data):
    with open('javv.csv', 'a', newline='', encoding="utf-8") as f:
        order = ['work', 'since']
        writer = csv.DictWriter(f, fieldnames=order)
        writer.writerow(data)

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    ts = soup.find('div', id='testimonial-2364-3-0-0').find_all('article')
    for t in ts:
        try:
            since = t.find('div', class_='author-details').find('p', class_='traxer-since').text.split()[2].strip()
        except:
            since = ''
        try:
            work = t.find('div', class_='author-details').find('p', class_='testimonial-author').text.strip()
        except:
            work = ''
        data = {'work': work, 'since': since}
        write_csv(data)

def main():
    pattern = 'https://catertrax.com/why-catertrax/traxers/page/{}'

    for i in range(1, 16):
        url = pattern.format(str(i))
        get_data(get_html(url))

if __name__ == '__main__':
    main()



