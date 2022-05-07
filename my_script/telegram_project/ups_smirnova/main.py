from pyrogram import Client, enums
from config import *
import time
import asyncio

async def get_user_info(client):
    async with client:
        for i in range(2):
            await client.send_chat_action('1242606918', enums.ChatAction.TYPING)
            await asyncio.sleep(2)
        time.sleep(1)
        await client.send_message('1242606918', 'Здравсвуйте!')
        time.sleep(2)
        for i in range(3):
            await client.send_chat_action('1242606918', enums.ChatAction.TYPING)
            await asyncio.sleep(4)
        time.sleep(2)
        await client.send_message('1242606918', 'Меня зовут Юлия. Я парфюмерный менеджер компании U Project Studio. Сообщаю активным пользователям интернет о существовании нашего бренда😊')
        time.sleep(5)
        for i in range(3):
            await client.send_chat_action('1242606918', enums.ChatAction.TYPING)
            await asyncio.sleep(3)
        time.sleep(2)
        await client.send_message('1242606918', 'Если интересна информация о нашей продукции, то задайте мне вопрос или посетите наш телеграмм канал @uprojectstudio')
        time.sleep(6)
        for i in range(3):
            await client.send_chat_action('1242606918', enums.ChatAction.TYPING)
            await asyncio.sleep(3)
        time.sleep(2)
        await client.send_message('1242606918', 'Также, информацию о нас вы найдете:\n⠀\n<b>Мы в ВК</b>: https://vk.com/u_project_studio\n⠀\n<b>Мы в Instagram</b>: https://www.instagram.com/uprojectstudio/')
        for i in range(2):
            await client.send_chat_action('1242606918', enums.ChatAction.TYPING)
            await asyncio.sleep(3)
        time.sleep(2)
        await client.send_message('1242606918', 'Приношу извинения если побеспокоила 🙏 Всего дорого😘')
        # for member in client.get_chat_members('uryupinsk'):
        #     id = member.user.id
        #     print(id)



if __name__ == '__main__':
    app = Client('account', api_id, api_hash)
    app.run(get_user_info(app))
    print('Запись всех данных успешно завершена!')
