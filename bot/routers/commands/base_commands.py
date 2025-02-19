from aiogram import types, Router, F
from aiogram.utils import markdown
from aiogram.filters import CommandStart, Command
from bot.keyboards.start_keyboard import *
from bot.templates.messages.base_messages import get_start_message

router = Router()

@router.message(F.text == "🏠 На главную")
@router.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer_photo(
        photo = 'https://i.pinimg.com/736x/20/43/f8/2043f8e7fe36c0c7fec8ecd5304724dc.jpg',
        caption = get_start_message(),
        reply_markup=get_start_inline_keyboard(),
        )

@router.message(F.text.startswith('inlinequery'))
async def handle_premiers(message: types.Message):
    await message.bot.send_message(chat_id=message.chat.id, text="Movie details")
    await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)

@router.message()
async def handle_premiers(message: types.Message):
    await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)