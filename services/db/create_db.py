import os
from sqlalchemy.ext.asyncio import create_async_engine


POSTGRESQL_USERNAME = os.getenv("POSTGRESQL_USERNAME")
POSTGRESQL_PASSWORD = os.getenv("POSTGRESQL_PASSWORD")
POSTGRESQL_DB_HOST = os.getenv("POSTGRESQL_DB_HOST")
POSTGRESQL_DB_NAME = os.getenv("POSTGRESQL_DB_NAME")

engine = create_async_engine(
	f"postgresql+asyncpg://{POSTGRESQL_USERNAME}:{POSTGRESQL_PASSWORD}@{POSTGRESQL_DB_HOST}/{POSTGRESQL_DB_NAME}",
)
