"""
Service layer for handling business logic related to member operations.
"""

from sqlalchemy.orm import Session
from model.member_models import Enroll
from model.member_schema import MemberRequest
from fastapi import HTTPException

def get_all_members(db: Session):
    """Fetch all members from the database."""
    return db.query(Enroll).all()

def get_member_by_id(db: Session, member_id: int):
    """Fetch a specific member by ID."""
    member = db.query(Enroll).filter(Enroll.id == member_id).first()
    if member is None:
        raise HTTPException(status_code=404, detail="Member not found")
    return member

def create_member(db: Session, member_req: MemberRequest):
    """Create a new member record."""
    member_model = Enroll(**member_req.model_dump())
    db.add(member_model)
    db.commit()
    db.refresh(member_model)
    return member_model

def update_member(db: Session, member_id: int, member_req: MemberRequest):
    """Update an existing member record."""
    member_model = db.query(Enroll).filter(Enroll.id == member_id).first()
    if member_model is None:
        raise HTTPException(status_code=404, detail="Member not found")

    for key, value in member_req.model_dump().items():
        setattr(member_model, key, value)

    db.commit()
    db.refresh(member_model)
    return member_model

def delete_member(db: Session, member_id: int):
    """Delete a member record."""
    member_model = db.query(Enroll).filter(Enroll.id == member_id).first()
    if member_model is None:
        raise HTTPException(status_code=404, detail="Member not found")

    db.delete(member_model)
    db.commit()
