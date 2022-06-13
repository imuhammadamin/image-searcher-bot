import logging 
import requests
from aiogram import Bot, Dispatcher, executor, types
from workWithApi import search
 
API_TOKEN = '5327165139:AAFiRiONZHI5n42Lc8GOHnKuJSZruktqNr4'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` command
    """
    await message.reply("Assalomu Alaykum!\nBu bot bilan siz istagan rasmingizni topa olasiz!\n\t")


@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends '/help' command
    """
    await message.reply("Yordam kerak bo'lsa @muhammadamins_robot ga yozing")


@dp.message_handler()
async def photo_sender(message: types.Message):
    word = message.text
    foto, capt = search(word)
    if foto != False and capt != False:
        await message.reply_photo(foto, caption = f"{capt}")
    else:
        await message.reply_to_message("Bunday rasm topilmadi")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
