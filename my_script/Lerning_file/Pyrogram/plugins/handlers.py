import asyncio
from pyrogram import Client, filters, enums

async def message_handler(client_obj, message_obj, text):
    print('Получено сообщение ожидаем 3с')
    await asyncio.sleep(3)
    await client_obj.read_chat_history(message_obj.chat.id)
    print('Прочитали сообщение пользователя...')
    print('Имитируем ввод сообщения...')
    await asyncio.sleep(3)
    await client_obj.send_chat_action(message_obj.chat.id, enums.ChatAction.TYPING)
    await asyncio.sleep(5)
    await client_obj.send_message(message_obj.chat.id, text)

@Client.on_message(filters.text)
async def text_handler(client, message):
    print(f'Пользователь отправил текст {message.text}')
    await message_handler(client, message, 'Вы отправили мне **текстовое сообщение**')

@Client.on_message(filters.sticker)
async def sticker_handler(client, message):
    print('Пользователь отправил стикер')
    await message_handler(client, message, 'Вы отправили мне **стикер**')