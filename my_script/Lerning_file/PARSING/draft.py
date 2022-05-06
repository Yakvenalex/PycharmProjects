import requests
from bs4 import BeautifulSoup

def get_html(url):
    user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.132 YaBrowser/22.3.1.895 Yowser/2.5 Safari/537.36'}
    r = requests.get(url, headers=user_agent)
    return r.text

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    za = soup.find('div', id='page_block_group_submain_info').find('h2').text.strip()
    print(za)

def main():
    url = 'https://vk.com/public211292791'
    get_data(get_html(url))

if __name__ == '__main__':
    main()