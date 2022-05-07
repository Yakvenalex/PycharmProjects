import time
from pyrogram import Client, filters, enums
from apscheduler.schedulers.background import BackgroundScheduler
from config import *

app = Client('account',
             api_id,
             api_hash)

with app:
    app.send_message('me', 'привет')