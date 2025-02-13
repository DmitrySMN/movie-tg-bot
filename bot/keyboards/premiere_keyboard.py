
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from ..services.movie_service import MovieService 

def get_premiere_keyboard():
    print(list(map(lambda x: x['nameRu'], MovieService.getPremierMovies('JUNE', 2021)['items'])))


get_premiere_keyboard()