from aiogram import Router, F
from aiogram.types import CallbackQuery, InputMediaPhoto
from aiogram.utils import markdown

from bot.keyboards.pagination_keyboard import get_pagination_keyboard


router = Router()

favorites = []

@router.callback_query(F.data.startswith("add-favorite-button"))
async def handle_favorite_button_callback(callback: CallbackQuery):
        movie_id = callback.data.split(':')[1] if len(callback.data.split(':')) > 1 else None
        if movie_id:  
            if (movie_id not in favorites):
                favorites.append(movie_id)
                await callback.answer(text="❕ Фильм добавлен в избранное")
            else:
                await callback.answer(text="❌ Фильм уже добавлен в избранное")
        else:
            await callback.answer(text="❌ Фильм HE добавлен в избранное")


@router.callback_query(F.data.startswith("favorites"))
async def handle_favorite_button_callback(callback: CallbackQuery):
    await callback.bot.edit_message_media(media=InputMediaPhoto(media='https://cdn.thememylogin.com/uploads/edd/2019/03/favorites.png', caption=markdown.bold("🤍 Ваши избранные фильмы")), chat_id=callback.message.chat.id, message_id=callback.message.message_id, reply_markup=get_pagination_keyboard(20))