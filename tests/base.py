import pytest

from services.db.database import reset_db



class BaseTest:


	@pytest.fixture(scope="function", autouse=True)
	async def clear_database(self):
		"""Фикстура для пересоздания тестовой БД перед каждым тестом."""
		await reset_db()
		yield
