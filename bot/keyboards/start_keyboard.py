from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, SwitchInlineQueryChosenChat


def get_start_keyboard():
    favorite_button = KeyboardButton(text="💙 Избранное")
    home_button = KeyboardButton(text="🏠 На главную")
    buttons_row = [favorite_button, home_button]
    keyboard = ReplyKeyboardMarkup(keyboard=[buttons_row], resize_keyboard=True)
    return keyboard

def get_start_inline_keyboard():
    premiers_button = InlineKeyboardButton(text="⭐ Премьеры", callback_data='premieres')
    search_button = InlineKeyboardButton(text="🔍 Поиск", switch_inline_query_current_chat="")
    favorites_button = InlineKeyboardButton(text="💜 Избранное", callback_data='favorites')
    recommendation_button = InlineKeyboardButton(text="🚩 Порекомендуй фильм", callback_data='recommendation-chat-button')
    all_movie_button = InlineKeyboardButton(text="📁 Популярные фильмы", callback_data='all-movie-button')
    inline_keyboard=InlineKeyboardMarkup(inline_keyboard=[[premiers_button, search_button], [favorites_button, all_movie_button], [recommendation_button]])
    return inline_keyboard