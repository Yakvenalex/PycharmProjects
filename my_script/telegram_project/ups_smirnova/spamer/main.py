from my_speac import *
from get_logins import logins
from pyrogram import Client, enums
from config import *
import time
import asyncio
import random

async def get_user_info(client):
    async with client:
        for id in logins:
            for i in range(2):
                await client.send_chat_action(id, enums.ChatAction.TYPING)
                await asyncio.sleep(2)
            time.sleep(1)
            await client.send_message(id, say_hello(hello))
            time.sleep(2)
            for i in range(3):
                await client.send_chat_action(id, enums.ChatAction.TYPING)
                await asyncio.sleep(4)
            time.sleep(2)
            await client.send_message(id, present(phrase))
            time.sleep(5)
            for i in range(3):
                await client.send_chat_action(id, enums.ChatAction.TYPING)
                await asyncio.sleep(3)
            time.sleep(2)
            await client.send_message(id, present_chanel(chan))
            time.sleep(6)
            for i in range(3):
                await client.send_chat_action(id, enums.ChatAction.TYPING)
                await asyncio.sleep(3)
            time.sleep(2)
            await client.send_message(id, poka_by(poka))
            time.sleep(random.randint(100, 300))

if __name__ == '__main__':
    app = Client('account', api_id, api_hash)
    app.run(get_user_info(app))
