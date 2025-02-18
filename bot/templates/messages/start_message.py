from aiogram.utils import markdown


def get_start_message() -> str:
    return f"{markdown.bold("🎦 Все что вы хотели знать о кинемотографе")}"