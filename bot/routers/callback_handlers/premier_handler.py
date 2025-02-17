from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.utils import markdown

from bot.keyboards.premiere_keyboard import get_premiere_keyboard

router = Router(name=__name__)

@router.callback_query(F.data == 'premieres')
async def handle_premiers_callback(callback: CallbackQuery):
    await callback.bot.send_message(chat_id=callback.message.chat.id, text=f'{markdown.bold('Премьеры за февраль 2025')}', reply_markup=get_premiere_keyboard())
    await callback.answer()

@router.callback_query(F.data.startswith("premier-movie-button"))
async def handle_premiere_button_click(callback: CallbackQuery):
    print(callback.data)
    await callback.bot.send_message(chat_id=callback.message.chat.id, text=f"button clicked")
    await callback.answer()