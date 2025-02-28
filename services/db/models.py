from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs



class Base(AsyncAttrs, DeclarativeBase):
	pass



class Users(Base):
	__tablename__ = "users"

	telegram_id = Column(Integer, primary_key=True, autoincrement=False)
	firstname = Column(String(100))
	lastname = Column(String(100))
	username = Column(String(100))
	phone_number = Column(String(20))
	language_id = Column(Integer, ForeignKey('languages.language_id'))
	subscription_id = Column(Integer, ForeignKey('subscription.subscription_id'))
	referall_link_id = Column(Integer, ForeignKey('referral_link.referral_link_id'))

	language = relationship("Languages")
	subscription = relationship("Subscription", uselist=False)
	referral_link = relationship("ReferralLink", uselist=False)



class Languages(Base):
	__tablename__ = "languages"

	language_id = Column(Integer, primary_key=True)
	language = Column(String(50), default="Русский")



class Subscription(Base):
	__tablename__ = "subscription"

	subscription_id = Column(Integer, primary_key=True)
	type = Column(String(30), default="free")
	payment_date = Column(Date)
	end_date = Column(Date)
	payment_method = Column(String(20))



class ReferralLink(Base):
	__tablename__ = "referral_link"

	referral_link_id = Column(Integer, primary_key=True)
	link = Column(String(50), unique=True)
	number_invitees = Column(Integer, default=0)












import os

from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, AsyncAttrs
from sqlalchemy.ext.asyncio import create_async_engine

from contextlib import asynccontextmanager

from config import config


engine = create_async_engine(
	f"postgresql+asyncpg://{config.POSTGRESQL_USERNAME}:{config.POSTGRESQL_PASSWORD}@{config.POSTGRESQL_DB_HOST}/{config.POSTGRESQL_DB_NAME}",
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



async def create_db():
	async with engine.begin() as conn:
		await conn.run_sync(Base.metadata.create_all)
		print("запуск бд")
