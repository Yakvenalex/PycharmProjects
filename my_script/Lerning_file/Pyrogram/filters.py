import time
from pyrogram import Client, filters, enums
from apscheduler.schedulers.background import BackgroundScheduler
from config import *
import asyncio

app = Client('account',
             api_id,
             api_hash)

def func(_, __, query):
    return not query.from_user.is_bot

static_data_filter = filters.create(func)

@app.on_message(static_data_filter)
def program_data(client, message):
    message.forward('me')

app.run()