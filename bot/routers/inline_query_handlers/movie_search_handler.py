from aiogram import Router, F
from aiogram.types import InlineQuery, InputTextMessageContent, InlineQueryResultArticle
from bot.services.movie_service import MovieService


router = Router()

@router.inline_query(F.query.len() > 0)
async def inline_query_title(inline_query: InlineQuery) -> None:
    title = inline_query.query
    items = map(lambda m: InlineQueryResultArticle(id=str(m['filmId']), title=m['nameRu'] if m['nameRu'] else m['nameEn'], input_message_content=InputTextMessageContent(message_text=f"inlinequery:{m['filmId']}"), description=f"🌟 {m['rating']} 📼 Год: {m['year']} 🔸 {m['genres'][0]['genre']}", thumbnail_url=m['posterUrl']) , MovieService.get_movie_by_title(title)['films'])
    await inline_query.answer(items, is_personal=True)


@router.inline_query()
async def inline_handler(inline_query: InlineQuery) -> None:
    movies = MovieService.get_sorted_movies()['items']
    items = list(map(lambda m: InlineQueryResultArticle(id=str(m['kinopoiskId']), title=m['nameRu'], input_message_content=InputTextMessageContent(message_text=f"inlinequery:{m['kinopoiskId']}"), description=f"🌟 {m['ratingKinopoisk']} 📼 Год: {m['year']} 🔸 {m['genres'][0]['genre']}", thumbnail_url=m['posterUrl']), movies))
    await inline_query.answer(items, is_personal=True)
