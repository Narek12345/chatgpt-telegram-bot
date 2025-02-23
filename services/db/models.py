from sqlalchemy import Column, Integer, String, BigInteger, Boolean, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from datetime import datetime
import asyncio

Base = declarative_base()

DATABASE_URL = "postgresql+asyncpg://user:password@localhost/dbname"

engine = create_async_engine(DATABASE_URL, echo=True)

AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session



class TelegramAccount(Base):
    __tablename__ = "telegram_accounts"

    telegram_id = Column(BigInteger, primary_key=True, unique=True, index=True)
    firstname = Column(String(100), nullable=True)
    lastname = Column(String(100), nullable=True)
    username = Column(String(100), nullable=True)
    phone_number = Column(String(20), nullable=True)
    is_admin = Column(Boolean, default=False)
    number_chatgpt_tokens = Column(Integer, default=50000)
    created_at = Column(DateTime, default=datetime.utcnow)

    messages = relationship("Message", back_populates="user", cascade="all, delete-orphan")


    @classmethod
    async def create(cls, db: AsyncSession, telegram_id: int, **kwargs):
        """Создает нового пользователя."""
        user = cls(telegram_id=telegram_id, **kwargs)
        db.add(user)
        await db.commit()
        await db.refresh(user)
        return user


    @classmethod
    async def get(cls, db: AsyncSession, telegram_id: int):
        """Получает пользователя по telegram_id."""
        result = await db.execute(select(cls).filter(cls.telegram_id == telegram_id))
        return result.scalars().first()


    async def update(self, db: AsyncSession, **kwargs):
        """Обновляет данные пользователя."""
        for key, value in kwargs.items():
            setattr(self, key, value)
        await db.commit()
        return self


    async def delete(self, db: AsyncSession):
        """Удаляет пользователя."""
        await db.delete(self)
        await db.commit()


    def get_tokens(self):
        """Получает количество токенов у пользователя."""
        return self.number_chatgpt_tokens


    async def update_tokens(self, db: AsyncSession, tokens: int):
        """Обновляет количество токенов пользователя."""
        self.number_chatgpt_tokens = tokens
        await db.commit()
        return self


    async def add_tokens(self, db: AsyncSession, tokens_to_add: int):
        """Добавляет токены пользователю."""
        self.number_chatgpt_tokens += tokens_to_add
        await db.commit()
        return self


    async def spend_tokens(self, db: AsyncSession, tokens_to_spend: int):
        """Списывает токены пользователя."""
        if self.number_chatgpt_tokens >= tokens_to_spend:
            self.number_chatgpt_tokens -= tokens_to_spend
            await db.commit()
            return self
        else:
            raise ValueError("Недостаточно токенов для выполнения операции.")



class Message(Base):
    __tablename__ = "messages"

    message_id = Column(BigInteger, primary_key=True, autoincrement=True)
    message_type = Column(String(10), nullable=False)
    message_text = Column(Text, nullable=False)
    token_usage = Column(Integer, default=0)
    is_bot = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    telegram_id = Column(BigInteger, ForeignKey("telegram_accounts.telegram_id", ondelete="CASCADE"))

    user = relationship("TelegramAccount", back_populates="messages")


    @classmethod
    async def create(cls, db: AsyncSession, telegram_id: int, message_type: str, message_text: str, token_usage: int = 0, is_bot: bool = False):
        """Создает сообщение."""
        message = cls(
            telegram_id=telegram_id,
            message_type=message_type,
            message_text=message_text,
            token_usage=token_usage,
            is_bot=is_bot
        )
        db.add(message)
        await db.commit()
        await db.refresh(message)
        return message


    @classmethod
    async def get_by_user(cls, db: AsyncSession, telegram_id: int):
        """Получает все сообщения пользователя."""
        result = await db.execute(select(cls).filter(cls.telegram_id == telegram_id))
        return result.scalars().all()


    @classmethod
    async def delete_by_user(cls, db: AsyncSession, telegram_id: int):
        """Удаляет все сообщения пользователя."""
        await db.execute(select(cls).filter(cls.telegram_id == telegram_id).delete())
        await db.commit()

