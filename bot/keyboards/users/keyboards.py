from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton


kb_list = [
	[KeyboardButton(text="👤 Мой аккаунт"), KeyboardButton(text="🧹 Очистить историю")],
	[KeyboardButton(text="⚙️ Настройки"), KeyboardButton(text="💎 Бесплатные токены")],
	[KeyboardButton(text="🚀 Премиум")],
]

keyboard = ReplyKeyboardMarkup(keyboard=kb_list, resize_keyboard=True)
