from aiogram import Router, F
from aiogram.types import CallbackQuery


router = Router()


@router.callback_query(F.data.startswith("add-favorite-button"))
async def handle_favorite_button_callback(callback: CallbackQuery):
    await callback.answer(text="❕ Фильм добавлен в избранное", show_alert=True)


@router.callback_query(F.data.startswith("favorites"))
async def handle_favorite_button_callback(callback: CallbackQuery):
    await callback.answer(text="Ваши избранные фильмы", show_alert=True)