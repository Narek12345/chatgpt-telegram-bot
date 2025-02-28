from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from .create_db import Base, get_session



class Users(Base):
	__tablename__ = "users"

	telegram_id = Column(Integer, primary_key=True, index=True)
	firstname = Column(String(100))
	lastname = Column(String(100))
	username = Column(String(100))
	phone_number = Column(String(20))
	language_id = Column(Integer, ForeignKey('language.id'))
	subscription_id = Column(Integer, ForeignKey('subscription.id'))
	referall_link_id = Column(Integer, ForeignKey('referral_link.id'))

	language = relationship("Languages")
	subscription = relationship("Subscription", uselist=False)
	referral_link = relationship("ReferralLink", uselist=False)



class ReferralLink(Base):
	__tablename__ = "referral_link"

	link = Column(String(50), unique=True)
	number_invitees = Column(Integer, default=0)
