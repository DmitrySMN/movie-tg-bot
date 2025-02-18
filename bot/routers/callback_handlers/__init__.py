from aiogram import Router
from .premier_handler import router as premier_handler_router
from .back_button_handler import router as back_button_router

router = Router()

router.include_routers(premier_handler_router, back_button_router)