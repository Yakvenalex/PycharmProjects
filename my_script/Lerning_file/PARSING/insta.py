from bs4 import BeautifulSoup
import csv

def get_day(d):
    day = d.split()[0]
    return day

def get_month(m):
    month = m.split()[1]
    return month

def get_year(y):
    year = y.split()[2]
    return year

def get_time(t):
    time = t.split()[4]
    return time

def write_csv(data):
    with open('followers.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'], data['link'], data['year'], data['month'], data['day'], data['time']))

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    folowers = soup.find('div', class_='_a706')

    for folower in folowers:
        name = folower.find('a').text
        link = folower.find('a').get('href')
        big_date = folower.find('div', class_='_a6-p').find_all('div')[2].text
        day = get_day(big_date)
        month = get_month(big_date)
        year = get_year(big_date)
        time = get_time(big_date)

        data = {'name': name, 'link':link, 'day': day, 'month': month, 'year': year, 'time': time}

        write_csv(data)

def main():
    html = open('followers.html', encoding='utf-8').read()
    get_data(html)
    print('Запись успешно завершена!')

if __name__ == '__main__':
    main()