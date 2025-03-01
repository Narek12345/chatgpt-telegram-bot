from services.db.models import Users
from services.db.create_engine import get_session



class UsersModelController(Users):

	@classmethod
	async def register(cls, **kwargs):
		"""Регистрирует пользователя."""
		new_user = cls(**kwargs)
		session = await get_session()
		await session.add(new_user)
		await session.commit()
