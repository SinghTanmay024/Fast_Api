"""
Defines Pydantic schemas for request and response validation.
"""

from pydantic import BaseModel, Field
from typing import Optional

class AddressRequest(BaseModel):
    state_code: str = Field(min_length=2, max_length=10, description="State code (e.g., CA, NY, TX)")
    zip_code: str = Field(min_length=5, max_length=10, description="ZIP code (e.g., 10001, 73301)")
    zip_plus_four_code: Optional[str] = Field(None, max_length=10, description="ZIP+4 code (optional)")
    zip_two_code: Optional[str] = Field(None, max_length=10, description="ZIP two code (optional)")
    county_code: Optional[str] = Field(None, max_length=10, description="County code (optional)")
    country_code: str = Field(min_length=2, max_length=10, description="Country code (e.g., US, CA)")
    foreign_postal_code: Optional[str] = Field(None, max_length=20, description="Foreign postal code (if applicable)")
    address_line1: str = Field(min_length=1, max_length=255, description="Primary address line")
    address_line2: Optional[str] = Field(None, max_length=255, description="Secondary address line (optional)")
    address_line3: Optional[str] = Field(None, max_length=255, description="Additional address line (optional)")
    address_line4: Optional[str] = Field(None, max_length=255, description="Additional address line (optional)")
    city_name: str = Field(min_length=1, max_length=255, description="City name")

