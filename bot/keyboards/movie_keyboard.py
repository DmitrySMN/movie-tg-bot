from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.services.movie_service import MovieService

def get_movie_keyboard(movie_id: int | None = None) -> InlineKeyboardMarkup:
    back_button = InlineKeyboardButton(text="↪️ Популярные фильмы", callback_data='all-movie-button')
    favorite_button = InlineKeyboardButton(text="💙 В избранное", callback_data=f'add-favorite-button:{movie_id}')
    #trailer_button = InlineKeyboardButton(text="▶️ Трейлер", callback_data="trailer-button")
    back_button_row = [back_button]
    favorite_button_row = [favorite_button]
    #trailer_button_row = [trailer_button]
    return InlineKeyboardMarkup(inline_keyboard=[favorite_button_row, back_button_row])

def get_list_movie_keyboard(list_of_id: list[int]) -> InlineKeyboardMarkup:
    movies = list(map(lambda i: MovieService.get_movie_by_id(i), list_of_id))
    movie_buttons = list(map(lambda m: InlineKeyboardButton(text=m['nameRu'], callback_data=f'premier-movie-button:{m['kinopoiskId']}'), movies))
    movie_buttons.append(InlineKeyboardButton(text="↪️ На главную", callback_data="back-start-button"))
    return InlineKeyboardMarkup(inline_keyboard=[[b] for b in movie_buttons])