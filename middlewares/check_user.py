from data import config, strings
from aiogram import types, BaseMiddleware


class CheckUserMiddleware(BaseMiddleware):
	async def __call__(self, handler, event: types.Message, data):
		from loader import app
		from db import user_repo

		async with app.state.conn_pool.acquire() as conn:
			user = await user_repo.get_user(conn=conn, tg_id=event.from_user.id)

			if user is None:
				await user_repo.add_user(
					conn=conn, 
					tg_id=event.from_user.id, 
					name=event.from_user.first_name,
					username=event.from_user.username
				)
				await event.answer(text=strings.user_added)
				return

			data['user'] = user
			data['is_admin'] = event.from_user.id in config.ADMINS
			return await handler(event, data)

