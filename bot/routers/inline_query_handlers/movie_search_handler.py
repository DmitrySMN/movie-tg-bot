import uuid
from aiogram import Router
from aiogram.types import InlineQuery, InputTextMessageContent, InlineQueryResultArticle
from bot.services.movie_service import MovieService

router = Router()

@router.inline_query()
async def inline_handler(inline_query: InlineQuery) -> None:
    movies = MovieService.get_sorted_movies()['items']
    items = list(map(lambda m: InlineQueryResultArticle(id=str(m['kinopoiskId']), title=m['nameRu'], input_message_content=InputTextMessageContent(message_text="content"), description=f"🌟 {m['ratingKinopoisk']} 📼 Год: {m['year']} 🔸 {m['genres'][0]['genre']}", thumbnail_url=m['posterUrl']), movies))
    await inline_query.answer(items, is_personal=True)