import requests
import csv

def get_text(url):
    r = requests.get(url)
    return r.text

def write_csv(data):
    with open('x.csv', 'a', newline='', encoding="utf-8") as f:
        order = ['name', 'url', 'description', 'traffic', 'percent']
        writer = csv.DictWriter(f, fieldnames=order)
        writer.writerow(data)

def get_data(text):
    all_info = text.strip().split('\n')[1:]

    for row in all_info:
        colums = row.strip().split('\t')
        name = colums[0]
        url = colums[1]
        description = colums[2]
        traffic = colums[3]
        percent = colums[4]

        data = {'name': name, 'url': url, 'description': description, 'traffic': traffic, 'percent': percent}
        write_csv(data)

def main():
    patter = 'https://www.liveinternet.ru/rating/ru//today.tsv?page={}'

    for i in range(1, 6):
        url = patter.format(str(i))
        get_data(get_text(url))

if __name__ == '__main__':
    main()