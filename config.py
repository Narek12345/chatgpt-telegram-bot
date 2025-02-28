import os

from dotenv import load_dotenv

load_dotenv()



class Config:
	TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

	POSTGRESQL_USERNAME = os.getenv("POSTGRESQL_USERNAME")
	POSTGRESQL_PASSWORD = os.getenv("POSTGRESQL_PASSWORD")
	POSTGRESQL_DB_HOST = os.getenv("POSTGRESQL_DB_HOST")
	POSTGRESQL_DB_NAME = os.getenv("POSTGRESQL_DB_NAME")



config = Config()
