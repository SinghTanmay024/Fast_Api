from pydantic import BaseModel
from datetime import date
from typing import Optional

class MemberAddressCreate(BaseModel):
    memberId: int
    addressId: int
    address_type_code: str
    effective_date: date
    termination_date: Optional[date] = None
    return_mail_indicator_code: str

