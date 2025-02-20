from config.db import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey


class MemberRace(Base):
    __tablename__ = "MEMBER_RACE"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    memberId = Column(Integer, ForeignKey("MEMBER.id", ondelete="CASCADE"), nullable=False)
    race_code = Column(String(10), nullable=False)
    race_effective_date = Column(Date, nullable=False)
    race_termination_date = Column(Date, nullable=True)

