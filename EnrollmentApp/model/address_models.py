from config.db import Base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship

class Address(Base):
    __tablename__ = 'ADDRESS'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    state_code = Column(String(10), nullable=False)
    zip_code = Column(String(10), nullable=False)
    zip_plus_four_code = Column(String(10), nullable=True)
    zip_two_code = Column(String(10), nullable=True)
    county_code = Column(String(10), nullable=True)
    country_code = Column(String(10), nullable=False)
    foreign_postal_code = Column(String(20), nullable=True)
    address_line1 = Column(String(255), nullable=False)
    address_line2 = Column(String(255), nullable=True)
    address_line3 = Column(String(255), nullable=True)
    address_line4 = Column(String(255), nullable=True)
    city_name = Column(String(255), nullable=False)
