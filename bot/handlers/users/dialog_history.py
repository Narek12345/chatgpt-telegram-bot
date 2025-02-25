from aiogram import Router, F
from aiogram.types import Message

from bot.keyboards.users.keyboards import keyboard


dialog_history_router = Router()

reset_dialog_history_text_ru = """
🧹 История чатов была очищена!

Чтобы перезапустить бота, отправьте команду /start.

Для доступа к «✨Дополнительным возможностям», используйте кнопки на клавиатуре ↘️ для включения генерации изображений, суперспособностей и других функций.
"""


@dialog_history_router.message(F.text == 'Очистить историю диалога')
async def reset_dialog_history_handler(message: Message):
	await message.answer("Диалог очищен", reply_markup=keyboard)


def register_dialog_history_router(dp):
	dp.include_router(dialog_history_router)
