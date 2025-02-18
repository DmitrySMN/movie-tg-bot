from aiogram.utils import markdown


def get_movie_message(name: str, year: int, genres: list, rating: float, description: str) -> str:
    return f'💥{markdown.bold(name)}\n\n📼 Год: {year} год\n🎬 Жанры: {genres[0]['genre']}, {genres[1]['genre'] if len(genres) > 1 else ""}\n⭐ Рейтинг: {str(rating).replace('.', '\.') if rating is not None else "Нет оценок"}\n\n📑 {markdown.italic(description.replace('.', '\.'))}'