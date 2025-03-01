import pytest

from services.db.controllers.users_model_controller import UsersModelController



class TestUsersModelController():


	@pytest.mark.asyncio
	async def test_register(self):
		test_data = {
			"telegram_id": 1111111111,
			"firstname": "firstname",
			"lastname": "lastname",
			"username": "username",
			"phone_number": "+77777777777",
		}
		await UsersModelController.register(**test_data)
