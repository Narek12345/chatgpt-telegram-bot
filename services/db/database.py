import os

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine

from contextlib import asynccontextmanager

from services.db.models import Base
from config import config



class Database:

	def __init__(self):
		self.database_url = f"postgresql+asyncpg://{config.POSTGRESQL_USERNAME}:{config.POSTGRESQL_PASSWORD}@{config.POSTGRESQL_DB_HOST}/{config.POSTGRESQL_DB_NAME}"
		self.engine = self.create_engine()


	def create_engine(self):
		engine = create_async_engine(self.database_url)
		return engine


	def async_session_generator(self):
		return sessionmaker(
			self.engine, expire_on_commit=False, class_=AsyncSession
		)


	@asynccontextmanager
	async def get_session(self):
		try:
			async_session = self.async_session_generator()

			async with async_session() as session:
				yield session
		except Exception as e:
			await session.rollback()
			raise e
		finally:
			await session.close()


	async def create_db(self):
		async with self.engine.begin() as conn:
			await conn.run_sync(Base.metadata.create_all)



database = Database()
