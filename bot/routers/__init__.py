from aiogram import Router
from .commands import router as commands_router
from .callback_handlers import router as callback_router
from .inline_query_handlers import router as inline_query_router

router = Router()
router.include_routers(
    callback_router,
    commands_router,
    inline_query_router)