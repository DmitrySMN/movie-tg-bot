from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def get_addition_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=get_addition_button())

def get_addition_button():
    back_button = InlineKeyboardButton(text="↪️ Назад", callback_data='back-button')
    favorite_button = InlineKeyboardButton(text="💙 В избранное", callback_data='favorite-button')
    back_button_row = [back_button]
    favorite_button_row = [favorite_button]
    return [favorite_button_row, back_button_row]