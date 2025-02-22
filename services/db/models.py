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
	username = Column(String(100), nullable=True, unique=True)
	phone_number = Column(String(20), nullable=True)
	is_admin = Column(Boolean, default=False)
	registration_date = Column(DateTime, default=datetime.utcnow)
	