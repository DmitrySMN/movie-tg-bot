import asyncio
import logging
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import CommandStart
from aiogram import types
from aiogram.enums import ParseMode
from aiogram.utils import markdown

load_dotenv()

bot = Bot(token=os.getenv('BOT_TOKEN'), parse_mode=ParseMode.MARKDOWN_V2)
dp = Dispatcher(storage=MemoryStorage())

# premiers_button = InlineKeyboardButton(text="Список премьер", callback_data='callback')

# favorites_button = InlineKeyboardButton(text="Избранные фильмы", callback_data='callback')

# keyboard = InlineKeyboardMarkup().add(premiers_button, favorites_button)

@dp.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer_photo(
        photo = 'https://m.media-amazon.com/images/I/A1hBTf09UkL.jpg',
        caption= f'{markdown.bold('🎥Все что вы хотели знать о кинемотографе')}'
        )

async def main():
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())