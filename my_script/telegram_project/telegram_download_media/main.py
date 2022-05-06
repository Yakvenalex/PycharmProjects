from pyrogram import Client
from config import *
from get_link_list import link_list
import requests
import os

def get_name(link):
    link = link.split('/')
    return link[-1]

app = Client('account', api_id, api_hash)

with app:
    history = app.get_chat_history('uprojectstudio')
    count = app.get_chat_history_count('uprojectstudio')
    print(f'Нашел в ТГ-канале: "Авторская парфюмерия U Project Studio" {count} сообщений')
    print('Приступаю к сохранению медиа на пк')

    for message in history:
        try:
            app.download_media(message)
            print(f'Медиа из сообщения с ID: {message.id} сохранено!')
        except:
            pass

print('Приступаю к сбору медиа по репостам')


os.chdir('downloads')
for i in link_list:
    name = get_name(i)
    img = requests.get(i).content
    with open(f'{name}', 'wb') as file:
        file.write(img)
    print(f'Медиа {name} сохранено!')
os.chdir('..')

print('Сохранение всех медиа из ТГ-канала "Авторская парфюмерия U Project Studio" завершено')
print('Все файлы сохранены в паке "downloads"')
print('Всего доброго!')