from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from bot.keyboards.users.keyboards import keyboard


start_router = Router()

start_bot_text_ru = """
Привет! 👋  Этот бот даёт вам доступ к лучшим нейросетям для создания текста, изображений, видео и песен

Я могу:

ℹ️ Отвечать на различные вопросы

📂 Работать с текстовыми файлами и табличными данными (например, CSV) — строить графики, выполнять вычисления и многое другое. Просто отправьте мне файл

🖼️ Генерировать изображения в режиме "Дополнительные возможности -> Изображения"

🔉 Конвертировать речь (аудио, видео, ссылки с Youtube) в текст в режиме "Дополнительные возможности -> Речь в текст". Я также поддерживаю голосовые сообщения, которые можно использовать как обычные команды (по аналогии с текстовыми запросами) во всех режимах

🧹 Если вы хотите очистить историю диалога, нажмите кнопку "Сбросить историю диалога" или отправьте команду /start

Советы по использованию: /help
"""


@start_router.message(Command("start"))
async def start_handler(message: Message):
	await message.answer(start_bot_text_ru, reply_markup=keyboard)


def register_start_router(dp):
	dp.include_router(start_router)
