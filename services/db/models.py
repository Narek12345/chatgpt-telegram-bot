from sqlalchemy import Column, String, Integer, Float, DateTime, ForeignKey
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
	payment_date = Column(DateTime, default=None)
	end_date = Column(DateTime, default=None)
	payment_method = Column(String(20), default=None)
	type_id = Column(Integer, ForeignKey('subscription_types.type_id'))

	type = relationship("SubscriptionTypes")



class ReferralLink(Base):
	__tablename__ = "referral_link"

	referral_link_id = Column(Integer, primary_key=True)
	link = Column(String(50), unique=True)
	number_invitees = Column(Integer, default=0)



class SubscriptionTypes(Base):
	__tablename__ = "subscription_types"

	type_id = Column(Integer, primary_key=True)
	type = Column(String(30), default="free")
	created_at = Column(DateTime(timezone=True), server_default=func.now())
	updated_at = Column(DateTime(timezone=True), onupdate=func.now())
	price_id = Column(Integer, ForeignKey("subscription_prices.price_id"))

	price = relationship("SubscriptionPrices", uselist=False)



class SubscriptionPrices(Base):
	__tablename__ = "subscription_prices"

	price_id = Column(Integer, primary_key=True)
	price = Column(Float)
	created_at = Column(DateTime(timezone=True), server_default=func.now())
	updated_at = Column(DateTime(timezone=True), onupdate=func.now())



class Models(Base):
	__tablename__ = "models"

	model_id = Column(Integer, primary_key=True)
	model_name_id = Column(Integer, ForeignKey("models_name.model_name.id"))
	model_type_id = Column(Integer, ForeignKey("model_types.model_type_id"))
	model_limit_type_id = Column(Integer, ForeignKey("model_limit_types.model_limit_type_id"))
	model_request_limit_id = Column(Integer, ForeignKey("model_request_limits.model_request_limit_id"))
	user_id = Column(Integer, ForeignKey("users.telegram_id"))

	model_name = relationship("ModelNames")
	model_type = relationship("ModelTypes")
	model_limit_type = relationship("ModelLimitTypes")
	model_request_limit = relationship("ModelRequestLimits", uselist=False)
	user = relationship("Users")



class ModelTypes(Base):
	__tablename__ = "model_types"

	model_type_id = Column(Integer, primary_key=True)
	model_type = Column(String(50))



class ModelLimitTypes(Base):
	__tablename__ = "model_limit_types"

	model_limit_type_id = Column(Integer, primary_key=True)
	limit_type = Column(String(50))



class ModelNames(Base):
	__tablename__ = "model_names"

	model_name_id = Column(Integer, primary_key=True)
	model_name = Column(String(50))



class ModelRequestLimits(Base):
	__tablename__ = "model_request_limits"

	model_request_limit_id = Column(Integer, primary_key=True)
	available_requests = Column(Integer)
	available_tokens = Column(Integer)
	number_requests = Column(Integer)
	number_tokens = Column(Integer)



class GeneratedObjects(Base):
	__tablename__ = "generated_objects"

	generated_object_id = Column(Integer, primary_key=True)
	object_name = Column(String(50))
	number_tokens_spent = Column(Integer, default=0)
	user_id = Column(Integer, ForeignKey("users.user_id"))

	user = relationship("Users")
