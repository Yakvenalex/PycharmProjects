import time
from pyrogram import Client, filters, enums
from apscheduler.schedulers.background import BackgroundScheduler
from config import *

app = Client('account',
             api_id,
             api_hash,
             plugins=plugins)
# app.run()

'''Создать канал'''
# with app:
#     app.create_channel('Название моего канала', 'Какое-то описание моего канала')

'''Удалить канал'''
# with app:
#     app.delete_channel('dsdasddsqw')

'''Инофрмация о канале'''
# with app:
#     res = app.get_chat("pyropypy")
#     print(res)

'''Количество подписчиков на канале'''
# with app:
#     res = app.get_chat_members_count("pyropypy")
#     print(res)

'''Количество всех моих диалогов'''
# with app:
#     res = app.get_dialogs_count()
#     print(res)

'''Cменить фото на канале'''
# with app:
#     with open('17.jpg', 'rb') as file:
#         app.set_chat_photo(-1001779009866, photo=file)

'''Удалить фото на канале'''
# with app:
#     app.delete_chat_photo(-1001779009866)

'''Отправить документ'''
# with app:
#     with open('file', 'rb') as file:
#         app.send_document('me', file)
#     app.send_document('me', 'https://i.pinimg.com/474x/b2/5a/15/b25a156dc271575e529c85086fcd4742.jpg')

'''Отправить фото'''
# with app:
#     with open('17.jpg', 'rb') as file:
#         #если так, то фото отправится как документ (лучшее качество)
#         app.send_document('me', file)
#     #если так, то фото отправится со сжатием (худшее качество) + отправка с сайта
#     app.send_photo('me', 'https://i.pinimg.com/474x/b2/5a/15/b25a156dc271575e529c85086fcd4742.jpg')

'''Работа с полученными сообщениями и декоратором'''
# @app.on_message()
# def echo(client, message):
#     print(message)
#     app.send_photo('-1001779009866', 'https://sun9-58.userapi.com/s/v1/if2/67pvqF7zyWNafFJSvQeo_W4uiQkw-9GSlu3XLRs7TRMjTEmyZ-3PfIY55K9rbCfafLLrpoSN5xrAY_kZQQoRSUSJ.jpg?size=1280x854&quality=95&type=album')
# app.run()

'''Получить информацию о себе'''
# with app:
#     me = app.get_chat('pyropypy')
#     print(me)

'''Получить информацию о пользователе'''
# with app:
#     user = app.get_users(1242606918)
#     print(user)

'''Получить id фото профиля'''
# with app:
#     all_photo = []
#     for photo in app.get_chat_photos('1242606918'):
#         all_photo.append(photo.file_id)
#     print(f'Я нашел тебе {len(all_photo)} фото в профиле твоей любимой девочки')
#     print('Введи номер фото, который мы отправим в наш телеграм-канал')
#     n = int(input('Номер фото: '))
#     app.send_photo('pyropypy', photo=all_photo[n-1])

'''Вносим правки в профиль'''
# with app:
#     app.update_profile(first_name='Alexey')
#     app.update_profile(last_name='Yakovenko')

'''Создаем свой фильтр'''

# def func(_, __, query):
#     return not query.from_user.is_bot
#
# static_data_filter = filters.create(func)
#
# @app.on_message(static_data_filter)
# def pyrogram_data(client, message):
#     message.forward('pyropypy')
#
# app.run()

'''Отправка сообщений со стилями'''
# app.set_parse_mode(enums.ParseMode.HTML)
# with app:
#     app.send_message("me", ('<b>Жирный текст</b>\n'
#                             '<i>Италик</i>\n'
#                             '<u>Подчеркивание</u>\n'
#                             '<s>Зачеркнем</s>\n'
#                             '<a href=\'https://docs.pyrogram.org/api/methods/set_parse_mode\'>URL</a>\n'
#                             '<code>code</code>\n\n'
#                             '<pre>'
#                             'for i in range(10):\n'
#                             '   print(i)'
#                             '</pre>')
#                      )

'''Планирование'''

def job():
    for i in range(1,10):
        app.send_message('me', f'{i}')

scheduler = BackgroundScheduler()
scheduler.add_job(job, 'interval', seconds=3)

scheduler.start()
app.run()