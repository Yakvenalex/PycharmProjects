import requests
from bs4 import BeautifulSoup

for o in range(0, 2):
    o+=1
    link = 'https://ruskino.ru/art/groups/actresses?page=' + str(o)

    responce = requests.get(link).text
    soup = BeautifulSoup(responce, 'lxml')

    block = soup.find('div', class_='main_content main_content_wide main_content_wide_full')
    blocka = block.find_all('div', class_='link-layer')

    for i in blocka:
        a = i['title']
        print(f'В файл добавлена {a}!')

        with open("file.txt","a") as f:
                f.write(a+"\n")