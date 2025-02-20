from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.utils import markdown

from bot.keyboards.pagination_keyboard import get_pagination_keyboard


router = Router()

favorites = []

@router.callback_query(F.data.startswith("add-favorite-button"))
async def handle_favorite_button_callback(callback: CallbackQuery):
        movie_id = callback.data.split(':')[1] if len(callback.data.split(':')) > 1 else None
        if movie_id:  
            favorites.append(movie_id)
            await callback.answer(text="❕ Фильм добавлен в избранное", show_alert=True)
        else:
            await callback.answer(text="❕ Фильм HE добавлен в избранное", show_alert=True)


@router.callback_query(F.data.startswith("favorites"))
async def handle_favorite_button_callback(callback: CallbackQuery):
    await callback.bot.send_message(chat_id=callback.message.chat.id, text=markdown.bold("🤍 Ваши избранные фильмы"), reply_markup=get_pagination_keyboard(20))