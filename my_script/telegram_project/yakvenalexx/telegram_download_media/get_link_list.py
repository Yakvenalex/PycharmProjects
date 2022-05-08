from pyrogram import Client

print('Запущен подготовительный этап...')

app = Client('account')
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