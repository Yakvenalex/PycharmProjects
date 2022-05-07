from pyrogram import Client
from config import *

app = Client('account', api_id, api_hash)

with app:
    app.send_message('AUTSA', 'Это сообщение сгенерировал наш бот Юлия Смирнова)')