from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton


def get_start_keyboard():
    favorite_button = KeyboardButton(text="💙 Избранное")
    home_button = KeyboardButton(text="🏠 На главную")
    buttons_row = [favorite_button, home_button]
    keyboard = ReplyKeyboardMarkup(keyboard=[buttons_row], resize_keyboard=True)
    return keyboard

def get_start_inline_keyboard():
    premiers_button = InlineKeyboardButton(text="⭐ Премьеры", callback_data='data')
    search_button = InlineKeyboardButton(text="🔍 Поиск", callback_data='data')
    inline_row = [premiers_button, search_button]
    inline_keyboard=InlineKeyboardMarkup(inline_keyboard=[inline_row])
    return inline_keyboard