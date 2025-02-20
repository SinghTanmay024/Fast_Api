from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base  # Import Base from your database setup

class MEMBER_EMAIL(Base):
    __tablename__ = "MEMBER_EMAIL"

    id = Column(Integer, primary_key=True, autoincrement=True)
    memberId = Column(Integer, ForeignKey("MEMBER.id"), nullable=False)  # Foreign key to MEMBER table
    email_type_code = Column(String(10), nullable=False)
    effective_date = Column(Date, nullable=False)
    termination_date = Column(Date, nullable=True)
    active_indicator_code = Column(String(10), nullable=False)
    email_address_text = Column(String(100), nullable=False)

