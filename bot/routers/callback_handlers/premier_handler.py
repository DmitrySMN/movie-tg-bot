from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.utils import markdown
from bot.keyboards.addition_keyboard import get_addition_keyboard
from bot.services.movie_service import MovieService
from bot.keyboards.premiere_keyboard import get_premiere_keyboard

router = Router()

@router.callback_query(F.data == 'premieres')
async def handle_premiers_callback(callback: CallbackQuery):
    await callback.bot.send_message(chat_id=callback.message.chat.id, text=f'{markdown.bold('Премьеры за февраль 2025')}', reply_markup=get_premiere_keyboard())
    await callback.answer()

@router.callback_query(F.data.startswith("premier-movie-button"))
async def handle_premiere_button_click(callback: CallbackQuery):
    movie = MovieService.get_movie_by_id(int(callback.data.split(':')[1]))
    await callback.bot.send_photo(chat_id=callback.message.chat.id, photo=movie["posterUrl"], caption=f'💥{markdown.bold(movie['nameRu'])}\n\nГод: 📼{movie['year']}', reply_markup=get_addition_keyboard())
    await callback.answer()