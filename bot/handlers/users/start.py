from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from bot.keyboards.users.keyboards import keyboard


start_router = Router()

start_bot_text_ru = """
Привет! 👋  Этот бот даёт вам доступ к лучшим нейросетям для создания текста, изображений, видео и песен.

Бесплатно доступны следующие модели: GPT 4o mini и Gemini 1.5 Pro.
"""


@start_router.message(Command("start"))
async def start_handler(message: Message):
	await message.answer(start_bot_text_ru, reply_markup=keyboard)


def register_start_router(dp):
	dp.include_router(start_router)
