import os
from threading import Thread
from pyrogram import Client, filters
from fastapi import FastAPI
import uvicorn

bot = Client(
    "ASTA-ROBOT-VERCEL",
    api_id=int(os.environ.get("ID")),
    api_hash=os.environ.get("HASH"),
    bot_token=os.environ.get("TOKEN")
)

app = FastAPI()

@bot.on_message(filters.command("start"))
async def start(client, m):
    await m.reply_text("Halo! Bot Pyrogram sudah berjalan di Vercel.")

# Route untuk halaman utama website
@app.get("/")
def read_root():
    return {"Hello": "world"}

def run_bot():
    bot.run()

if __name__ == "__main__":
    Thread(target=run_bot).start()
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
