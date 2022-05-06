from bs4 import BeautifulSoup
import csv

def get_good_login(login):
    return login[1:-2]

def write_csv(data):
    with open('parfumbuyer.csv', 'a', newline='', encoding="utf-8") as f:
        order = ['login', 'name_page', 'link']
        writer = csv.DictWriter(f, fieldnames=order)
        writer.writerow(data)

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    folowwers = soup.find_all('li', class_='wo9IH')
    p = len(folowwers)
    print(f'Я для тебя спарсил информацию на {p} подписчиков parfumbuyer!')
    for folowwer in folowwers:
        try:
            name_page = folowwer.find(class_='wFPL8').text.strip()
        except:
            name_page = ''

        link = 'https://www.instagram.com' + folowwer.find('a', class_="notranslate _0imsa").get('href')
        login = get_good_login(folowwer.find('a', class_="notranslate _0imsa").get('href'))

        data = {'login': login, 'name_page': name_page, 'link': link}
        write_csv(data)

def main():
    html = open('1234.html', encoding='utf-8').read()
    get_data(html)
    print('Поздравляю, запись данных завершена упешно!')
if __name__ == '__main__':
    main()