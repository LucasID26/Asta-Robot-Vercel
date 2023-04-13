import os
from threading import Thread
from pyrogram import Client, filters,idle
from fastapi import FastAPI
import uvicorn


with open("uffizzi.yml", "r") as f:
    config = yaml.safe_load(f)["pyrogram"]

# Buat instance Pyrogram Client
bot = Client(**config)

#bot = Client(
   # "ASTA-ROBOT-VERCEL",
    #api_id=int(os.environ.get("ID")),
   # api_hash=os.environ.get("HASH"),
  #  bot_token=os.environ.get("TOKEN"))

#app = FastAPI()

@bot.on_message(filters.command("start"))
async def start(client, m):
    await m.reply_text("Halo! Bot Pyrogram sudah berjalan di Vercel.")


bot.run()
# Route untuk halaman utama website
#@app.get("/")
#def read_root():
  #  return {"Hello": "world"}

#def run_bot():
   # bot.start()
    #idle()
   # bot.stop()

#if __name__ == "__main__":
  #  Thread(target=run_bot).start()
   # uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
