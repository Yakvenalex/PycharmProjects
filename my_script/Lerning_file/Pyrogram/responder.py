from pyrogram import Client
from config import *

app = Client('account', api_id, api_hash, plugins=plugins)
app.run()