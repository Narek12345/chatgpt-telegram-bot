from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton


kb_list = [
	[KeyboardButton(text="Очистить историю диалога"), KeyboardButton(text="Отправить длинное сообщение")],
	[KeyboardButton(text="✨Дополнительные возможности"), KeyboardButton(text="⚙️Версия ИИ")],
	[KeyboardButton(text="💾Чаты"), KeyboardButton(text="💲Баланс"), KeyboardButton(text="🇷🇺Язык")],
	[KeyboardButton(text="Текущий режим: текси ИИ")]
]

keyboard = ReplyKeyboardMarkup(keyboard=kb_list, resize_keyboard=True)
