from pydantic import BaseModel
from datetime import date
from typing import Optional

class MemberRaceBase(BaseModel):
    memberId: int
    race_code: str
    race_effective_date: date
    race_termination_date: Optional[date] = None