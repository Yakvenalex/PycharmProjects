from pyrogram import Client
from config import api_id, api_hash

print('Запущен подготовительный этап...')

app = Client('account', api_id, api_hash)
link_list = []

with app:
    history = app.get_chat_history('uprojectstudio')
    for message in history:
        try:
            if 'https://telegra.ph' in message.web_page.url:
                url = message.web_page.url
                link_list.append(url)
        except:
            pass