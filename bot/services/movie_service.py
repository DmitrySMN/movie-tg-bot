import requests, os
from dotenv import load_dotenv

load_dotenv(dotenv_path='../../.env')

class MovieService:

    @staticmethod
    def get_premier_movies(month: str, year: int) -> dict:
        response = requests.get(
            url=f'https://kinopoiskapiunofficial.tech/api/v2.2/films/premieres?year={year}&month={month}',
            headers={'accept': 'application/json',
                    'X-API-KEY': os.getenv('KINOPOISK_API_TOKEN')})
        return response.json()

    @staticmethod
    def get_movie_by_id(id: int) -> dict:
        response = requests.get(
            url=f'https://kinopoiskapiunofficial.tech/api/v2.2/films/{id}',
            headers={'accept': 'application/json',
                    'X-API-KEY': os.getenv('KINOPOISK_API_TOKEN')})
        return response.json()