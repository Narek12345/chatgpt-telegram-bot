from .users.start import register_start_router
from .users.dialog_history import register_dialog_history_router


def register_all_routers(dp):
	register_start_router(dp)
	register_dialog_history_router(dp)
