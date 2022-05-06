import requests
from bs4 import BeautifulSoup
import csv

my_list = []
my_new_list = []
my_new_list_2 = []
my_new_list_3 = []

def name():

    for o in range(100, 150):
        o+=1
        link = 'https://ruskino.ru/art/groups/actresses?page=' + str(o)

        responce = requests.get(link).text
        soup = BeautifulSoup(responce, 'lxml')

        block = soup.find('div', class_='main_content main_content_wide main_content_wide_full')
        blocka = block.find_all('div', class_='link-layer')

        for i in blocka:
            a = i['title']
            my_list.append(a)

    for cc in my_list:
        return cc

name()

for i in my_list:
    y = i.split()
    y[0] = y[0] + '+'
    y[1] = y[1] + '+'
    my_new_list.append(y)

for y in my_new_list:
    y[0] = y[0] + y[1]
    y.pop(1)
    my_new_list_2.append(y)

list_family = []
list_name = []

while len(my_new_list_3) != 1000:
    for i in my_new_list_2:
        for x in i:
            my_new_list_3.append(x)



    for i in range(0, len(my_new_list_3)):
        link = 'https://search.yahoo.com/search?p=' + my_new_list_3[i] + 'инстаграм'
        name = my_new_list_3[i]


        r = requests.get(link).text
        soup = BeautifulSoup(r, 'lxml')
        h1 = soup.find_all('div', class_='dd algo algo-sr relsrch fst richAlgo')

        for i in h1:
            url_insta = i.find('div', class_='compTitle options-toggle').find('h3').find('a').get('href')

            data = {'name': name, 'insta': url_insta}
            print(data)


            with open('insta.csv', 'a', newline='') as f:
                writer = csv.writer(f)

                list_data = [data['name'], data['insta']]
                writer.writerow(list_data)