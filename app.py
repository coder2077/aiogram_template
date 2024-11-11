import asyncio

from aiogram import types
from fastapi import Request

from handlers import dp
from loader import app, bot, logger


@app.post('/webhook', tags=['Bot webhook'], summary='Webhook for the bot')
async def webhook_bot(request: Request):
	try:
		update = types.Update(**await request.json())

		asyncio.create_task(dp.feed_webhook_update(bot, update))
	except Exception as e:
		logger.error(f'Error processing webhook: {e}')

	return {'status': 'success'}

