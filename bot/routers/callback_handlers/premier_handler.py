from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.utils import markdown

from keyboards.addition_keyboard import get_addition_keyboard

router = Router()

@router.callback_query()
async def handle_premiers_callback(callback: CallbackQuery):
    if (callback.data == 'premieres'):
        await callback.bot.send_message(chat_id=callback.message.chat.id, text=f'{markdown.bold('Премьеры за февраль 2025')}', reply_markup=get_addition_keyboard())

    await callback.answer()