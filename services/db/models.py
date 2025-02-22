from sqlalchemy import Column, Integer, String, BigInteger, Boolean, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from datetime import datetime


Base = declarative_base()



class TelegramAccount(Base):
	__tablename__ = "telegram_accounts"

	telegram_id = Column(BigInteger, primary_key=True, unique=True, index=True)
	firstname = Column(String(100), nullable=True)
	lastname = Column(String(100), nullable=True)
	username = Column(String(100), nullable=True)
	phone_number = Column(String(20), nullable=True)
	is_admin = Column(Boolean, default=False)
	created_at = Column(DateTime, default=datetime.utcnow)

	messages = relationship("Message", back_populates="user", cascade="all, delete-orphan")
	tokens = relationship("ChatGPTToken", back_populates="user", cascade="all delete-orphan")


	@classmethod
	def create(cls, db: Session, telegram_id: int, **kwargs):
		"""Создает нового пользователя."""
		user = cls(telegram_id=telegram_id, **kwargs)
		db.add(user)
		db.commit()
		db.refresh()
		return user


	@classmethod
	def get(cls, db: Session, telegram_id: int):
		"""Получает пользователя по telegram_id."""
		return db.query(cls).filter(cls.telegram_id == telegram_id).first()


	def update(self, db: Session, **kwargs):
		"""Обновляет данные пользователя."""
		for key, value in kwargs.items():
			setattr(self, key, value)
		db.commit()
		return self



class Message(Base):
	__tablename__ = "messages"

	message_id = Column(BigInteger, primary_key=True, autoincrement=True)
	message_type = Column(String(10), nullable=False)
	message_text = Column(Text, nullable=False)
	token_usage = Column(Integer, default=0)
	is_bot = Column(Boolean, default=False)
	created_at = Column(DateTime, default=datetime.utcnow)
	telegram_id = Column(BigInteger, ForeignKey("telegram_accounts.telegram_id", on_delete="CASCADE"))

	user = relationship("TelegramAccount", back_populates="messages")



class ChatGPTToken(Base):
	__tablename__ = "chatgpt_tokens"

	id = Column(String(100), primary_key=True, unique=True)
	number_of_tokens = Column(Integer, default=0)
	telegram_id = Column(BigInteger, ForeignKey("telegram_accounts.telegram_id", on_delete="CASCADE"))
