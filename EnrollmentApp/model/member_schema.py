"""
Defines Pydantic schemas for request and response validation.
"""

from pydantic import BaseModel, Field
from typing import Optional

class MemberRequest(BaseModel):
    dob: str = Field(description="Date of birth must be in YYYY-MM-DD format")
    gender: str = Field(description="Gender must be Male, Female, or Other")
    firstname: str = Field(min_length=1, max_length=255, description="First name cannot be empty")
    middlename: Optional[str] = Field(None, max_length=255, description="Middle name is optional")
    lastname: str = Field(min_length=1, max_length=255, description="Last name cannot be empty")
    relation_ship_code: str = Field(min_length=1, max_length=10, description="Relationship code cannot be empty")
    parent_id: Optional[int] = Field(None, ge=0, description="Parent ID must be a non-negative integer")
