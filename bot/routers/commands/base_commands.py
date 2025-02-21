import os
from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from bot.keyboards.movie_keyboard import get_movie_keyboard
from bot.keyboards.start_keyboard import *
from bot.models.users import Users
from bot.templates.messages.base_messages import *
from bot.services.movie_service import MovieService

router = Router()

load_dotenv(dotenv_path='../../../.env')

engine = create_engine(os.getenv('DATABASE_URI'))

Session = sessionmaker(bind=engine)
session = Session()

@router.message(F.text == "🏠 На главную")
@router.message(CommandStart())
async def handle_start(message: types.Message):
    try:
        user = session.query(Users).filter(Users.username == message.from_user.username).first()
        if user is None:
            new_user = Users(username=message.from_user.username, favorites=[])
            session.add(new_user)
            session.commit()
            session.close()
    except BaseException as err:
        print(err)
    finally:
        session.close()
        await message.answer_photo(
            photo = 'https://i.pinimg.com/736x/20/43/f8/2043f8e7fe36c0c7fec8ecd5304724dc.jpg',
            caption = get_start_message(),
            reply_markup=get_start_inline_keyboard(),
            )
        await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)


@router.message(F.text.startswith('inlinequery'))
async def handle_premiers(message: types.Message):
    movie_id=message.text.split(':')[1]
    movie = MovieService.get_movie_by_id(movie_id)
    await message.bot.send_photo(chat_id=message.chat.id, photo=movie['posterUrl'], caption=get_movie_message(name=movie['nameRu'], year=movie['year'], genres=movie['genres'], rating=movie['ratingKinopoisk'], description=movie['description']), reply_markup=get_movie_keyboard(movie_id=movie_id))
    await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)

@router.message()
async def handle_premiers(message: types.Message):
    await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    