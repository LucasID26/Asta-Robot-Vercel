from config import bot
from pyrogram import filters,idle


@bot.on_message(filters.command('start'))
async def start(client,m):
    await m.reply_text("Start")


bot.start()
