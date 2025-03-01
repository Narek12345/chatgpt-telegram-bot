import pytest

from services.db.database import reset_database



class BaseTest:


	@pytest.fixture(scope="function", autouse=True)
	async def clear_database(self):
		"""Фикстура для пересоздания БД перед каждым тестом."""
		await reset_database()
		yield
