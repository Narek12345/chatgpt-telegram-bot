import asyncio

from bot.create_bot import bot, dp
from bot.handlers import register_all_routers
from services.db.database import database


register_all_routers(dp)


async def main():
	await database.create_db()
	await dp.start_polling(bot)


if __name__ == "__main__":
	asyncio.run(main())
