from config import bot
from pyrogram import filters,idle,Client
from flask import Flask
from threading import Thread

app = Flask("")

@app.route("/")
def root():
    return {"message": "ASTA-ROBOT RUN!"}


@bot.on_message(filters.command('start'))
async def start(client,m):
    await m.reply_text("Start")


def run_flask():
    app.run(host='0.0.0.0',port=8080)

def run_thread():
    Thread(target=run_flask).start()

def run():
    run_thread()
    bot.start()

run()
