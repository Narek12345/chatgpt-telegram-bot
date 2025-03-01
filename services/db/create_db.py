from services.db.models import Base
from services.db.create_engine import engine


async def create_db():
	async with engine.begin() as conn:
		await conn.run_sync(Base.metadata.create_all)
