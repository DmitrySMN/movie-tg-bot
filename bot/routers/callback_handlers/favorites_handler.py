from aiogram import Router, F
from aiogram.types import CallbackQuery, InputMediaPhoto
from aiogram.utils import markdown
from bot.crud import update_user_favorites
from bot.keyboards.pagination_keyboard import get_pagination_keyboard
from bot.config import Session

router = Router()
session = Session()

@router.callback_query(F.data.startswith("add-favorite-button"))
async def handle_favorite_button_callback(callback: CallbackQuery):
        movie_id = callback.data.split(':')[1] if len(callback.data.split(':')) > 1 else None
        try:
            if movie_id:  
                update_user_favorites(session, callback.from_user.username, movie_id)
                await callback.answer(text="❕ Фильм добавлен в избранное")
            else:
                await callback.answer(text="❌ Фильм HE добавлен в избранное")
        except BaseException as err:
             print(err) 

@router.callback_query(F.data.startswith("favorites"))
async def handle_favorite_button_callback(callback: CallbackQuery):
    await callback.bot.edit_message_media(media=InputMediaPhoto(media='https://cdn.thememylogin.com/uploads/edd/2019/03/favorites.png', caption=markdown.bold("🤍 Ваши избранные фильмы")), chat_id=callback.message.chat.id, message_id=callback.message.message_id, reply_markup=get_pagination_keyboard(20))