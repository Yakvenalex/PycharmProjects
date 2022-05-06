import csv

def get_csv():
    with open('tetyana.csv', 'a', newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(['имя', 'возраст', 'рейтинг', 'ссылка'])

get_csv()



