from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.db import get_db
from model.member_race_schema import MemberRaceBase
from services.member_race_service import (
    create_member_race, get_member_race, get_member_races_by_member_id, delete_member_race
)

router = APIRouter(prefix="/member_races", tags=["Member Races"])

@router.post("/")
def create_member_race_route(member_race: MemberRaceBase, db: Session = Depends(get_db)):
    return create_member_race(db, member_race)

@router.get("/{member_race_id}", response_model=MemberRaceBase)
def get_member_race_route(member_race_id: int, db: Session = Depends(get_db)):
    race = get_member_race(db, member_race_id)
    if not race:
        raise HTTPException(status_code=404, detail="Member race not found")
    return race

@router.get("/member/{member_id}", response_model=list[MemberRaceBase])
def get_member_races_by_member_id_route(member_id: int, db: Session = Depends(get_db)):
    return get_member_races_by_member_id(db, member_id)


@router.delete("/{member_race_id}")
def delete_member_race_route(member_race_id: int, db: Session = Depends(get_db)):
    deleted_race = delete_member_race(db, member_race_id)
    if not deleted_race:
        raise HTTPException(status_code=404, detail="Member race not found")
    return {"message": "Member race deleted successfully"}
