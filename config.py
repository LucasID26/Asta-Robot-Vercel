from pyrogram import Client
import os

ID = os.environ.get("ID")
HASH = os.environ.get("HASH")
TOKEN = os.environ.get("TOKEN")

bot = Client("Asta-Robot-Vercel", 
             api_id=ID,
             api_hash=HASH,
             bot_token=TOKEN,
             in_memory=True)
