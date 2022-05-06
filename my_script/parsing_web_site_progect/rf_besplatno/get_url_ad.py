import requests
from bs4 import BeautifulSoup

list_link_ad = []

pattern = 'https://россия.бесплатныеобъявления.рф/uslugi/?obyavleniya={}'

for i in range(1, 11):
    url = pattern.format(str(i))
    r = requests.get(url).text
    soup = BeautifulSoup(r, 'lxml')
    block = soup.find_all('h4')

    for u in block:
        link = 'https://россия.бесплатныеобъявления.рф' + u.find('a').get('href')
        list_link_ad.append(link)

print(list_link_ad)
print(len(list_link_ad))