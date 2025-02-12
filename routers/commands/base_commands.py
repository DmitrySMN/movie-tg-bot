from aiogram import types, Router
from aiogram.utils import markdown
from aiogram.filters import CommandStart

router = Router()
# premiers_button = InlineKeyboardButton(text="Список премьер", callback_data='callback')

# favorites_button = InlineKeyboardButton(text="Избранные фильмы", callback_data='callback')

# keyboard = InlineKeyboardMarkup().add(premiers_button, favorites_button)

@router.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer_photo(
        photo = 'https://m.media-amazon.com/images/I/A1hBTf09UkL.jpg',
        caption= f'{markdown.bold('🎥Все что вы хотели знать о кинемотографе')}'
        )