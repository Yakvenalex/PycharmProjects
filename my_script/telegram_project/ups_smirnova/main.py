from pyrogram import Client
from config import *

app = Client('account', api_id, api_hash)

with app:
    app.send_message('yakvenalexx', 'Привет!!!')