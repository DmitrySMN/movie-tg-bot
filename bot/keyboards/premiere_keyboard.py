from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.services.movie_service import MovieService

def get_premiere_keyboard():
    premier_buttons = list(map(lambda x: InlineKeyboardButton(text=x['nameRu'], callback_data='premier-movie-button'), MovieService.getPremierMovies('JUNE', 2021)['items']))
    print(premier_buttons)
    return InlineKeyboardMarkup(inline_keyboard=[premier_buttons])