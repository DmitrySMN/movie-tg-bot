from aiogram import Router
from .commands import router as commands_router

router = Router()
router.include_router(commands_router)