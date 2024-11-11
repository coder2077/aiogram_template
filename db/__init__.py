import asyncpg
from data import pg_config


async def setup_database():
	return await asyncpg.create_pool(
		user=pg_config.user, 
		password=pg_config.password, 
		database=pg_config.database, 
		host=pg_config.host, 
		port=pg_config.port, 
		min_size=pg_config.MIN_POOL_SIZE, 
		max_size=pg_config.MAX_POOL_SIZE
	)


async def create_tables(conn: asyncpg.Connection):

	await conn.execute("""CREATE TABLE IF NOT EXISTS users (
	id BIGINT PRIMARY KEY, 
	name VARCHAR(64), 
	username VARCHAR(32), 
	created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP)""")

