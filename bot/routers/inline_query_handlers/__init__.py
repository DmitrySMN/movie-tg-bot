from aiogram import Router
from .movie_search_handler import router as movie_search_router

router = Router()

router.include_router(movie_search_router)