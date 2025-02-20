from pydantic import BaseModel
from datetime import date
from typing import Optional

### Schema for Creating a Member Email
class MemberEmailCreate(BaseModel):
    memberId: int
    email_type_code: str
    effective_date: date
    termination_date: Optional[date] = None
    active_indicator_code: str
    email_address_text: str
