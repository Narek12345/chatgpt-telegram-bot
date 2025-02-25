from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton


kb_list = [
	[KeyboardButton(text="👤 Мой аккаунт"), KeyboardButton(text="🧹 Очистить историю")],
	[KeyboardButton(text="⚙️ Настройки"), KeyboardButton(text="🎭 GPT - Роли")],
	[KeyboardButton(text="🚀 Премиум"), KeyboardButton(text="📚 Для учебы и работы")],
]

keyboard = ReplyKeyboardMarkup(keyboard=kb_list, resize_keyboard=True)
