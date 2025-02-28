import os

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine

from contextlib import asynccontextmanager


POSTGRESQL_USERNAME = os.getenv("POSTGRESQL_USERNAME")
POSTGRESQL_PASSWORD = os.getenv("POSTGRESQL_PASSWORD")
POSTGRESQL_DB_HOST = os.getenv("POSTGRESQL_DB_HOST")
POSTGRESQL_DB_NAME = os.getenv("POSTGRESQL_DB_NAME")

engine = create_async_engine(
	f"postgresql+asyncpg://{POSTGRESQL_USERNAME}:{POSTGRESQL_PASSWORD}@{POSTGRESQL_DB_HOST}/{POSTGRESQL_DB_NAME}",
)


def async_session_generator():
	return sessionmaker(
		engine, class_=AsyncSession
	)


@asynccontextmanager
async def get_session():
	try:
		async_session = async_session_generator()

		async with async_session() as session:
			yield session
	except Exception as e:
		await session.rollback()
		raise e
	finally:
		await session.close()
