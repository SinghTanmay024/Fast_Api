from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base

class MemberAddress(Base):
    __tablename__ = "MEMBER_ADDRESS"

    id = Column(Integer, primary_key=True, autoincrement=True)
    memberId = Column(Integer, ForeignKey("MEMBER.id"), nullable=False)
    addressId = Column(Integer, ForeignKey("ADDRESS.id"), nullable=False)
    address_type_code = Column(String(10), nullable=False)
    effective_date = Column(Date, nullable=False)
    termination_date = Column(Date, nullable=True)
    return_mail_indicator_code = Column(String(10), nullable=False)
