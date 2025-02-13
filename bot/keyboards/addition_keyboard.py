from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_addition_keyboard():
    back_button = InlineKeyboardButton(text="↪️ На главную", callback_data='back')
    inline_row = [back_button]
    inline_keyboard=InlineKeyboardMarkup(inline_keyboard=[inline_row])
    return inline_keyboard