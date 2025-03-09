from aiogram import Router, F
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from bot.services.movie_service import MovieService

router = Router()

@router.callback_query(F.data.startswith("similar-button"))
async def similar_button_handler(callback: CallbackQuery):
    movie_title = callback.data.split(':')[1]
    movie_year = int(callback.data.split(':')[2])
    similar_movies = MovieService.get_similar_movies(movie_title, movie_year)['result'][1:]
    print(similar_movies)
    similar_movie_buttons = list(map(lambda m: InlineKeyboardButton(text=m['title'], callback_data='similar-movie-button'), similar_movies))
    similar_movie_buttons.append(InlineKeyboardButton(text="↪️ Назад", callback_data=f'markup-back-button'))
    await callback.bot.edit_message_reply_markup(chat_id=callback.message.chat.id,
                                          message_id=callback.message.message_id,reply_markup=InlineKeyboardMarkup(inline_keyboard=[[m] for m in similar_movie_buttons]))