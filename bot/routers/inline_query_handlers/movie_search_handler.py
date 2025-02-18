from aiogram import Router
from aiogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent
import uuid

router = Router()

@router.inline_query()
async def inline_handler(inline_query: InlineQuery) -> None:
    item = InlineQueryResultArticle(id=str(uuid.uuid4()), title="Item title!", input_message_content=InputTextMessageContent(message_text="message text"))
    await inline_query.answer([item], is_personal=True)