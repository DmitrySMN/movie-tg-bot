from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.keyboards.addition_keyboard import get_addition_keyboard
from bot.services.movie_service import MovieService

def get_premiere_keyboard():
    premier_buttons = list(map(lambda x: InlineKeyboardButton(text=x['nameRu'], callback_data='premier-movie-button'), MovieService.get_premier_movies('FEBRUARY', 2025)['items']))
    print(premier_buttons)
    return InlineKeyboardMarkup(inline_keyboard=[[b] for b in premier_buttons])
