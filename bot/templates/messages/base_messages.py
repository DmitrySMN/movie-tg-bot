from aiogram.utils import markdown


def get_start_message() -> str:
    return f"{markdown.bold("🎦 Все что вы хотели знать о кинемотографе")}"

def get_movie_message(name: str, year: int, genres: list, rating: float, description: str) -> str:
    return f'💥{markdown.bold(name)}\n\n📼 Год: {year} год\n🎬 Жанры: {genres[0]['genre']}, {genres[1]['genre'] if len(genres) > 1 else ""}\n⭐ Рейтинг: {str(rating).replace('.', '\.') if rating is not None else "Нет оценок"}\n\n📑 {markdown.italic(description.replace('.', '\.'))}'

def get_all_movies_message():
    return markdown.bold("📎 Список всех фильмов")