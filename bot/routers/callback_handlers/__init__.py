from aiogram import Router
from .premier_handler import router as premier_handler_router
from .back_button_handler import router as back_button_router
from .favorites_handler import router as favorite_router
from .similar_button_handler import  router as similar_router

router = Router()

router.include_routers(premier_handler_router, back_button_router, favorite_router, similar_router)