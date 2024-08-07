import logging

from aiogram import Bot, Dispatcher, executor, types
import requests

API_TOKEN = '7296636465:AAGyGSPSno1GXdJyvkL6rtlL33OZcY3xtQg'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("""Hi!\nI'm Spotify!\nPowered by aiogram.
        /artist
        /albom
        /song
    """)


@dp.message_handler(commands=['song'])
async def send_welcome(message: types.Message):
    song = requests.get(f'http://127.0.0.1:8000/song/')
    for song in song.json():
        await message.reply(f"""
        Title:{song['title']}\n
        """)


@dp.message_handler(commands=['albom'])
async def send_welcome(message: types.Message):
    album = requests.get(f'http://127.0.0.1:8000/albom/')
    for album in album.json():
        await message.reply(f"""
        Title:{album['title']}\n
        Artist:{album['artist']}
        """)


@dp.message_handler(commands=['artist'])
async def send_welcome(message: types.Message):
    artist = requests.get(f'http://127.0.0.1:8000/artist/')
    for artist in artist.json():
        await message.reply(f"""
        Name:{artist['first_name']}\n
        Last_name:{artist['last_name']}
        """)


@dp.message_handler()
async def send_welcome(message: types.Message):
    search_data = message.text
    song = requests.get(f'http://127.0.0.1:8000/song/?search={search_data}')
    if song.json():
        for song in song.json():
            await message.reply(f"""      
            Title:{song['title'].title()}
            Artist:{song['albom']['artist']['first_name']}
            Artist:{song['albom']['artist']['last_name']}
            Albom:{song['albom']['title']}
            
            """)
    else:
        await message.reply("qoshiq topilmadi")


@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
