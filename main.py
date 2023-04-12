from config import bot
from pyrogram import filters,idle,Client
from fastapi import FastAPI
from threading import Thread

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "ASTA-ROBOT RUN!"}


@bot.on_message(filters.command('start'))
async def start(client,m):
    await m.reply_text("Start")


def run_fast():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    #app.run(host='0.0.0.0',port=8080)

def run_thread():
    Thread(target=run_fast).start()

def run():
    run_thread()
    bot.start()
    idle()
    bot.stop()

run()
