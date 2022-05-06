import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    title = soup.find(class_='site-title').text
    return title

def main():
    url = 'https://wordpress.org/'
    print(get_data(get_html(url)))



if __name__ == '__main__':
    main()