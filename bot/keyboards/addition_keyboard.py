from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def get_addition_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[get_addition_button()])

def get_addition_button():
    back_button = InlineKeyboardButton(text="↪️ Назад", callback_data='back')
    inline_row = [back_button]
    return inline_row