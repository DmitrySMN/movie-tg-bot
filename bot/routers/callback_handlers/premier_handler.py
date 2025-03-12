from aiogram import Router, F
from aiogram.types import CallbackQuery, InputMediaPhoto
from aiogram.utils import markdown
from bot.keyboards.movie_keyboard import get_movie_keyboard
from bot.services.movie_service import MovieService
from bot.keyboards.premiere_keyboard import get_premiere_keyboard
from bot.templates.messages.base_messages import get_movie_message

router = Router()

@router.callback_query(F.data == 'premieres')
async def handle_premiers_callback(callback: CallbackQuery):
    await callback.bot.edit_message_media(media=InputMediaPhoto(media='https://cbx-prod.b-cdn.net/COLOURBOX65908436.jpg?width=800&height=800&quality=70', caption=markdown.bold("Премьеры за март 2025 года")), chat_id=callback.message.chat.id, message_id=callback.message.message_id, reply_markup=get_premiere_keyboard())
    await callback.answer()

@router.callback_query(F.data.startswith("premier-movie-button"))
async def handle_premiere_button_click(callback: CallbackQuery):
    movie = MovieService.get_movie_by_id(int(callback.data.split(':')[1]))
    await callback.bot.edit_message_media(media=InputMediaPhoto(
        media=movie['posterUrl'],
        caption=get_movie_message(movie['nameRu'], movie['year'], movie['genres'], movie['ratingKinopoisk'], movie['description'])),
                                          chat_id=callback.message.chat.id,
                                          message_id=callback.message.message_id,
                                          reply_markup=get_movie_keyboard(movie_id=movie['kinopoiskId'], movie_title=movie['nameOriginal']))
    await callback.answer()