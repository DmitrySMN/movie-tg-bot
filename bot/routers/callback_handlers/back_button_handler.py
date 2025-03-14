from aiogram import Router, F
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import CallbackQuery, InputMediaPhoto
from bot.keyboards.movie_keyboard import get_list_movie_keyboard, get_movie_keyboard
from bot.keyboards.pagination_keyboard import *
from bot.keyboards.start_keyboard import get_start_inline_keyboard
from bot.services.movie_service import MovieService
from bot.templates.messages.base_messages import *

router = Router()

@router.callback_query(F.data.startswith("back-start-button"))
async def handle_premiers_callback(callback: CallbackQuery):
    media = InputMediaPhoto(media='https://i.pinimg.com/736x/20/43/f8/2043f8e7fe36c0c7fec8ecd5304724dc.jpg', caption=get_start_message())
    await callback.bot.edit_message_media(media=media, chat_id=callback.message.chat.id, message_id=callback.message.message_id, reply_markup=get_start_inline_keyboard())
    await callback.answer()

@router.callback_query(F.data.startswith("all-movie-button"))
async def handle_back_button_callback(callback: CallbackQuery):
    movies_id = list(map(lambda m: m['kinopoiskId'] ,MovieService.get_sorted_movies()['items']))
    builder = InlineKeyboardBuilder(get_pagination_markup(20))
    # builder.add()
    media = InputMediaPhoto(media='https://payload.cargocollective.com/1/11/367710/13568488/CINEMA-CLASSICS-POSTER_RUTGERS_1340_c.jpg', caption=get_all_movies_message())
    await callback.bot.edit_message_media(media=media, chat_id=callback.message.chat.id, message_id=callback.message.message_id, reply_markup=get_list_movie_keyboard(movies_id))

@router.callback_query(F.data == "markup-back-button")
async def handle_markup_back_button_callback(callback: CallbackQuery):
    await callback.bot.edit_message_reply_markup(chat_id=callback.message.chat.id, message_id=callback.message.message_id, reply_markup=get_movie_keyboard())