from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, SwitchInlineQueryChosenChat


def get_pagination_keyboard(total_pages: int):
    prev_button = InlineKeyboardButton(text="◀️", callback_data='prev')
    page_number = InlineKeyboardButton(text=f"1/{total_pages}", callback_data="page_number")
    next_button = InlineKeyboardButton(text="▶️", callback_data='next')
    inline_keyboard=InlineKeyboardMarkup(inline_keyboard=[[prev_button, page_number, next_button], [InlineKeyboardButton(text='↪️ На главную', callback_data='back-start-button')]])
    return inline_keyboard

def get_pagination_markup(total_pages: int) -> list:
    prev_button = InlineKeyboardButton(text="◀️", callback_data='prev')
    page_number = InlineKeyboardButton(text=f"1/{total_pages}", callback_data="page_number")
    next_button = InlineKeyboardButton(text="▶️", callback_data='next')
    return [[prev_button, page_number, next_button], [InlineKeyboardButton(text='↪️ На главную', callback_data='back-start-button')]]