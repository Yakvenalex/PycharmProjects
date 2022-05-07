from pyrogram import Client, enums
from config import *
import time
import asyncio
import random

async def get_user_info(client):
    async with client:
        async for member in client.get_chat_members('chatkzn116'):
            id = member.user.id
            for i in range(2):
                await client.send_chat_action(id, enums.ChatAction.TYPING)
                await asyncio.sleep(2)
            time.sleep(1)
            await client.send_message(id, 'Здравсвуйте!')
            time.sleep(2)
            for i in range(3):
                await client.send_chat_action(id, enums.ChatAction.TYPING)
                await asyncio.sleep(4)
            time.sleep(2)
            await client.send_message(id, 'Меня зовут Юлия. Я парфюмерный менеджер компании U Project Studio. Сообщаю активным пользователям интернет о существовании нашего бренда😊')
            time.sleep(5)
            for i in range(3):
                await client.send_chat_action(id, enums.ChatAction.TYPING)
                await asyncio.sleep(3)
            time.sleep(2)
            await client.send_message(id, 'Если интересна информация о нашей продукции, то задайте мне вопрос или посетите наш телеграмм канал @uprojectstudio')
            time.sleep(6)
            for i in range(3):
                await client.send_chat_action(id, enums.ChatAction.TYPING)
                await asyncio.sleep(3)
            time.sleep(2)
            await client.send_message(id, 'Также, информацию о нас вы найдете:\n⠀\n<b>Мы в ВК</b>: https://vk.com/u_project_studio\n⠀\n<b>Мы в Instagram</b>: https://www.instagram.com/uprojectstudio/')
            for i in range(2):
                await client.send_chat_action(id, enums.ChatAction.TYPING)
                await asyncio.sleep(3)
            time.sleep(2)
            await client.send_message(id, 'Приношу извинения если побеспокоила 🙏 Всего дорого😘')
            time.sleep(random.randint(100, 300))

if __name__ == '__main__':
    app = Client('account', api_id, api_hash)
    app.run(get_user_info(app))
