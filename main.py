#from config import bot
from pyrogram import filters,idle,Client
from fastapi import FastAPI


ID = os.environ.get("ID")
HASH = os.environ.get("HASH")
TOKEN = os.environ.get("TOKEN")

bot = Client("Asta-Robot-Vercel", 
             api_id=ID,
             api_hash=HASH,
             bot_token=TOKEN,
             in_memory=True)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "ASTA-ROBOT RUN!"}


@bot.on_message(filters.command('start'))
async def start(client,m):
    await m.reply_text("Start")


bot.run()
