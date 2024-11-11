from loader import logger
from asyncpg import Connection


async def add_user(conn: Connection, tg_id: int, name: str, username: str):
	sql = "INSERT INTO users (id, name, username) VALUES ($1, $2, $3)"
	try:
		await conn.execute(sql, tg_id, name, username)
	except Exception as e:
		logger.error(f"Adding user failed: {e}")


async def update_user(conn: Connection, tg_id: int, data: dict):
	set_clause = ", ".join(f"{key} = ${i + 2}" for i, key in enumerate(data.keys()))
	sql = f"UPDATE users SET {set_clause} WHERE id = $1"
	values = [value for value in data.values()]
	try:
		await conn.execute(sql, tg_id, *values)
	except Exception as e:
		logger.error(f"Updating user failed: {e}")


async def get_user(conn: Connection, tg_id: int):	
	sql = "SELECT * FROM users WHERE id = $1"
	return await conn.fetchrow(sql, tg_id)

