import time
from pyrogram import Client, filters, enums
from config import *
import asyncio

app = Client('account', api_id, api_hash)

async def message_handler(client, text):
    print('Получено сообщение ожидаем 3с')
    await asyncio.sleep(3)
    await client.read_chat_history('your_virtual_assistant')
    print('Прочитали сообщение пользователя...')
    print('Имитируем ввод сообщения...')
    await asyncio.sleep(3)
    await client.send_chat_action('your_virtual_assistant', enums.ChatAction.TYPING)
    await asyncio.sleep(3)
    await client.send_message('your_virtual_assistant', text)


@app.on_message(filters.text)
async def echo(client, message):
    if 'привет' in message.text.lower() or 'здравсвуйте' in message.text.lower() or 'добр' in message.text.lower():
        await message_handler(client, 'Здравсвуйте. Чем могу быть полезен?')
    elif 'бот' in message.text.lower():
        await message_handler(client, 'Мне обидно 😞 С чего вы взяли что я бот!?')
        time.sleep(4)
        await app.send_chat_action('your_virtual_assistant', enums.ChatAction.TYPING)
        time.sleep(4)
        await app.send_message('your_virtual_assistant', 'Сейчас вам отправлю голосовое, чтоб вы не думали что я бот')
        time.sleep(4)
        await app.send_chat_action('your_virtual_assistant', enums.ChatAction.RECORD_AUDIO)
        time.sleep(4)
        await app.send_voice('your_virtual_assistant', 'audio.ogg')
    elif 'фото' in message.text.lower():
        await message_handler(client, 'Подбираю вам красивую фоточку😊')
        time.sleep(5)
        await app.send_photo('your_virtual_assistant', 'https://i.pinimg.com/474x/b2/5a/15/b25a156dc271575e529c85086fcd4742.jpg')
        time.sleep(2)
        await app.send_message('your_virtual_assistant', 'Как вам фотография?')

@app.on_message(filters.sticker)
async def sticker_handler(client, message):
    time.sleep(3)
    await app.send_sticker('your_virtual_assistant', 'AnimatedSticker.tgs')

app.run()