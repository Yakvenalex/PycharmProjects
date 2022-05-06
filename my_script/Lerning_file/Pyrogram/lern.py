import time
from pyrogram import Client, filters, enums
from apscheduler.schedulers.background import BackgroundScheduler
from config import *
import requests
import os

def good_name(link):
    link = link.split('/')
    return link[-1]

app = Client('account', api_id, api_hash)

'''Загрузка медиа с сообщений группы'''
with app:
    history = app.get_chat_history('uprojectstudio')
    count = app.get_chat_history_count('uprojectstudio')
    print(f'В ТГ-канале: "Авторская парфюмерия U Project Studio" {count} сообщений')
    print('Приступаю к сохранению медиа на пк')

    for message in history:
        try:
            app.download_media(message)
            print(f'Медиа из сообщения с ID: {message.id} сохранено!')
        except:
            pass
with app:
    os.chdir('downloads')
    for message in history:
        try:
            if 'https://telegra.ph' in message.web_page.url:
                url = message.web_page.url
                name = good_name(message.web_page.url)
                img = requests.get(url).content
                with open(f'{name}', 'wb') as file:
                    file.write(img)
                print(f'Медиа из сообщения с ID: {message.id} сохранено!')
        except:
            pass

    os.chdir('..')
    print('Сохранение всех медиа из ТГ-канала "Авторская парфюмерия U Project Studio" завершено')
    print('Все файлы сохранены в паке "downloads"')
    print('Всего доброго!')