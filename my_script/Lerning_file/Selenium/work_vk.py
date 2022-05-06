from bs4 import BeautifulSoup
import csv

def write_csv(data):
    with open('vk_first_result.csv', 'a', newline='', encoding="utf-8") as f:
        order = ['name', 'state', 'city', 'link']
        writer = csv.DictWriter(f, fieldnames=order)
        writer.writerow(data)

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    peoples = soup.find_all('div', class_='people_row search_row clear_fix')

    for people in peoples:
        link = 'https://vk.com' + people.find('a').get('href')

        try:
            name = people.find('img').get('alt').strip()
        except:
            name = 'Нет данных'

        try:
            state = people.find_all(class_ ='labeled')[1].text.split()[1]
        except:
            state = 'Нет данных'

        try:
            city = people.find_all(class_ ='labeled')[1].text.split()[0][:-1]
        except:
            city = 'Нет данных'

        data = {'name': name, 'state': state, 'city': city, 'link': link}

        print(data)



def main():
    html = open('1234.html', encoding='utf-8').read()
    get_data(html)

if __name__ == '__main__':
    main()