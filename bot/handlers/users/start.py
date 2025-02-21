from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

start_router = Router()


@start_router.message(Command("start"))
async def start_handler(message: Message):
	await message.answer("Hello")


def register_start_router(dp):
	dp.include_router(start_router)
