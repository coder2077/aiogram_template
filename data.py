import re


class config:
	""" Bot config """

	BOT_TOKEN = "Your bot token"
	ADMINS = [] # List of admin IDs

	WEBHOOK_URL = 'https://your-domain.com' + '/webhook'


class pg_config:
	""" Potsgres database config """

	host = "127.0.0.1"
	port = 5432
	user = "postgres"
	password = "postgres"
	database = "db_name"
	
	MIN_POOL_SIZE = 5
	MAX_POOL_SIZE = 20


class strings:
	""" Bot texts """

	def escape_markdown(text: str) -> str:
		""" Escape special characters for Telegram Markdown v1. """
		special_chars = r'[_*\[`]'
		return re.sub(special_chars, r'\\\g<0>', text)

	welcome = "Welcome, You are already in my database!"

	user_added = "I saved you to my database!"

