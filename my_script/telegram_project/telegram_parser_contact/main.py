from pyrogram import Client
from config import *
import csv


def write_csv(data):
    with open('belittled_users.csv', 'a', newline='', encoding="utf-8") as f:
        order = ['id', 'login', 'first_name', 'last_name', 'is_bot']
        writer = csv.DictWriter(f, fieldnames=order)
        writer.writerow(data)


def get_user_info(client):
    with client:
        for member in client.get_chat_members(-1001415526465):
            user = member.user
            id = user.id
            username = user.username
            first_name = user.first_name
            last_name = user.last_name
            is_bot = user.is_bot
            if is_bot:
                is_bot = 'бот'
            else:
                is_bot = 'не бот'
            data = {'id': id, 'login': username, 'first_name': first_name, 'last_name': last_name, 'is_bot': is_bot}
            write_csv(data)
            print(f'Данные юзера с ID: {id} успешно записаны в файл CSV')


if __name__ == '__main__':
    app = Client('account', api_id, api_hash)
    get_user_info(app)
    print('Запись всех данных успешно завершена!')
