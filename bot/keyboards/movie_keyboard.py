from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def get_movie_keyboard(movie_id: int | None = None):
    back_button = InlineKeyboardButton(text="↪️ Назад", callback_data='back-button')
    favorite_button = InlineKeyboardButton(text="💙 В избранное", callback_data=f'add-favorite-button:{movie_id}')
    trailer_button = InlineKeyboardButton(text="▶️ Трейлер", callback_data="trailer-button")
    back_button_row = [back_button]
    favorite_button_row = [favorite_button]
    trailer_button_row = [trailer_button]
    return InlineKeyboardMarkup(inline_keyboard=[favorite_button_row, trailer_button_row, back_button_row])