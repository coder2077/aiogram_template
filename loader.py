import logging

from fastapi import FastAPI
from contextlib import asynccontextmanager

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties

from data import config
from middlewares import setup_middlewares
from db import setup_database, create_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
	logger.info('[#] Bot is starting up...')
	try:
		await bot.set_webhook(config.WEBHOOK_URL, drop_pending_updates=True)
	except Exception as e:
		logger.error(f'Webhook setup failed: {e}')

	app.state.conn_pool = await setup_database()
	await create_tables(conn=app.state.conn_pool)
	setup_middlewares(dp=dp)

	yield

	await app.state.conn_pool.close()
	await bot.delete_webhook(drop_pending_updates=True)
	logger.info('[#] Bot is shutting down...')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(lifespan=lifespan)
bot = Bot(token=config.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN))
storage = MemoryStorage()
dp = Dispatcher(storage=storage)