from aiogram import types, Router, F
from aiogram.utils import markdown
from aiogram.filters import CommandStart, Command
from bot.keyboards.movie_keyboard import get_movie_keyboard
from bot.keyboards.start_keyboard import *
from bot.templates.messages.base_messages import *
from bot.services.movie_service import MovieService

router = Router()

@router.message(F.text == "🏠 На главную")
@router.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer_photo(
        photo = 'https://i.pinimg.com/736x/20/43/f8/2043f8e7fe36c0c7fec8ecd5304724dc.jpg',
        caption = get_start_message(),
        reply_markup=get_start_inline_keyboard(),
        )

@router.message(F.text.startswith('inlinequery'))
async def handle_premiers(message: types.Message):
    movie_id=message.text.split(':')[1]
    movie = MovieService.get_movie_by_id(movie_id)
    await message.bot.send_photo(chat_id=message.chat.id, photo=movie['posterUrl'], caption=get_movie_message(name=movie['nameRu'], year=movie['year'], genres=movie['genres'], rating=movie['ratingKinopoisk'], description=movie['description']), reply_markup=get_movie_keyboard(movie_id=movie_id))
    await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)

@router.message()
async def handle_premiers(message: types.Message):
    await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)