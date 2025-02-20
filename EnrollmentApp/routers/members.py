"""
API routes for managing members.
"""

from fastapi import APIRouter, Depends, Path
from sqlalchemy.orm import Session
from config.db import get_db
from model.member_schema import MemberRequest
from services.member_service import (
    get_all_members,
    get_member_by_id,
    create_member,
    update_member,
    delete_member,
)

router = APIRouter()

@router.get("/members", status_code=200)
async def get_all_member(db: Session = Depends(get_db)):
    return get_all_members(db)

@router.get("/members/{id}", status_code=200)
async def get_member(id: int = Path(gt=0), db: Session = Depends(get_db)):
    return get_member_by_id(db, id)

@router.post("/members", status_code=201)
async def create_new_member(member_req: MemberRequest, db: Session = Depends(get_db)):
    return create_member(db, member_req)

@router.put("/members/{id}", status_code=204)
async def update_existing_member(member_req: MemberRequest, db: Session = Depends(get_db),id: int = Path(gt=0)):
    return update_member(db, id, member_req)

@router.delete("/members/{id}", status_code=204)
async def remove_member(id: int, db: Session = Depends(get_db)):
    return delete_member(db, id)
