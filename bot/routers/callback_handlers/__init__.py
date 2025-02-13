from aiogram import Router
from .premier_handler import router as premier_handler_router

router = Router()

router.include_router(premier_handler_router)