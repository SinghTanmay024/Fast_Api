from config.db import Base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship

class Enroll(Base):
    __tablename__='MEMBER'

    id = Column(Integer, primary_key=True, index=True)
    dob = Column(Date, nullable=False)
    gender = Column(String(10), nullable=False)
    firstname = Column(String(255), nullable=False)
    middlename = Column(String(255), nullable=True)
    lastname = Column(String(255), nullable=False)
    relation_ship_code = Column(String(10), nullable=False)
    parent_id = Column(Integer, nullable=True)
