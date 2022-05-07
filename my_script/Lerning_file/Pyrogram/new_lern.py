import time
from pyrogram import Client, filters, enums
from apscheduler.schedulers.background import BackgroundScheduler
from config import *
import asyncio

app = Client('account',
             api_id,
             api_hash)

# async def main():
#     async with app:
#         for _ in range(3):
#             await app.send_chat_action(5332290640, enums.ChatAction.TYPING)
#             await asyncio.sleep(5)
#         await asyncio.sleep(5)
#         await app.send_message(5332290640, 'my_text')

# async def main():
#     async with app:
#         async for message in app.search_messages('1242606918', query="люблю"):
#             if message.from_user.id == 1242606918:
#                 print(f'{message.text} - написала любимая')
#             else:
#                 print(f'{message.text} - написал я')
# app.run(main())

# with app:
#     for i in app.get_chat_photos(1242606918):
#         app.send_photo('me', i.file_id)


