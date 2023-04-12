import os
from pyrogram import Client, filters
from fastapi import FastAPI

bot = Client(
    "ASTA-ROBOT-VERCEL", 
    api_id=os.environ.get("ID"), 
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

#if __name__ == "__main__":
   # import uvicorn
   # uvicorn.run(app, host="0.0.0.0", port=5000)
bot.run()
