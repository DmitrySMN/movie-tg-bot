import requests, os
from dotenv import load_dotenv

load_dotenv(dotenv_path='../.env')

class MovieService:

    @staticmethod
    def getPremierMovies(month: str, year: int) -> dict:
        response = requests.get(
            url=f'https://kinopoiskapiunofficial.tech/api/v2.2/films/premieres?year={year}&month={month}',
            headers={'accept': 'application/json',
                    'X-API-KEY': os.getenv('KINOPOISK_API_TOKEN')})
        return response.json()

# get names from json
# print(list(map(lambda x: x['nameRu'], MovieService.getPremierMovies('JUNE', 2021)['items'])))
