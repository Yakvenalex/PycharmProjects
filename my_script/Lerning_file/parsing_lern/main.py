import requests
from bs4 import BeautifulSoup

def get_html(url):
    r = requests.get(url)
    return r.text

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    h1 = soup.find(class_='site-title').text
    return h1

def main():
    url = 'https://wordpress.org/'
    g = get_html(url)
    print(get_data(g))



if __name__ == '__main__':
    main()