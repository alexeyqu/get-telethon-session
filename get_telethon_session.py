from telethon.sessions import StringSession
from telethon import TelegramClient

api_id = 0000000
api_hash = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

with TelegramClient(StringSession(), api_id, api_hash) as client:
    print(client.session.save())
