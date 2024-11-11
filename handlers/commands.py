from aiogram import types
from aiogram.filters import CommandStart

from loader import dp
from data import strings


@dp.message(CommandStart())
async def cmd_start(message: types.Message, user) -> None:
	""" This handler receives messages with `/start` command """

	await message.answer(text=strings.welcome)

