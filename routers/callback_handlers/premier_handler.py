from aiogram import Router, F
from aiogram.types import CallbackQuery

router = Router()

@router.callback_query()
async def handle_premiers_callback(callback: CallbackQuery):
    if (callback.data == 'premieres'):
        await callback.bot.send_message(chat_id=callback.message.chat.id, text='Премьеры')

    await callback.answer()