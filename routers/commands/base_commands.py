from aiogram import types, Router, F
from aiogram.utils import markdown
from aiogram.filters import CommandStart, Command
from keyboards.start_keyboard import *

router = Router()
# premiers_button = InlineKeyboardButton(text="Список премьер", callback_data='callback')

# favorites_button = InlineKeyboardButton(text="Избранные фильмы", callback_data='callback')

# keyboard = InlineKeyboardMarkup().add(premiers_button, favorites_button)


@router.message(F.text == "🏠 На главную")
@router.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer_photo(
        photo = 'https://i.pinimg.com/736x/20/43/f8/2043f8e7fe36c0c7fec8ecd5304724dc.jpg',
        caption= f'{markdown.bold('🎥Все что вы хотели знать о кинемотографе')}',
        reply_markup=get_start_inline_keyboard(),
        )
    
# @router.message(Command('premiers'))
# async def handle_premiers(message: types.Message):
#     await message.answer(text='Премьеры')