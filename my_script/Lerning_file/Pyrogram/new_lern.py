import time
from pyrogram import Client, filters, enums
from apscheduler.schedulers.background import BackgroundScheduler
from config import *
import asyncio

app = Client('account',
             api_id,
             api_hash)
my_text = 'Как бы я хотел сделать: отправляется действие, потом как оно заканчивается, отправляется файл. Но получается так, что действие длится 5 секунд, а потом еще 5 секунд занимает отправка файла, и это время пользователь не понимает, это бот завис или файл еще отправляется. Как увеличить время действия до непосредственной отправки файла?'


# async def main():
#     async with app:
#         for _ in range(3):
#             await app.send_chat_action(5332290640, enums.ChatAction.TYPING)
#             await asyncio.sleep(5)
#         await asyncio.sleep(5)
#         await app.send_message(5332290640, my_text)

# async def main():
#     async with app:
#         async for message in app.search_messages('1242606918', query="люблю"):
#             if message.from_user.id == 1242606918:
#                 print(f'{message.text} - написала любимая')
#             else:
#                 print(f'{message.text} - написал я')
# app.run(main())