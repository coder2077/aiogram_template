from aiogram import Dispatcher
from .check_user import CheckUserMiddleware


def setup_middlewares(dp: Dispatcher):
	dp.message.middleware(CheckUserMiddleware())

