from aiogram.types import InlineKeyboardButton

def get_addition_keyboard():
    back_button = InlineKeyboardButton(text="↪️ Назад", callback_data='back')
    inline_row = [back_button]
    #inline_keyboard=InlineKeyboardMarkup(inline_keyboard=[inline_row])
    return inline_row