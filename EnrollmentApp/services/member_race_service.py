from sqlalchemy.orm import Session
from model.member_race import MemberRace

def create_member_race(db: Session, member_race: MemberRace):
    db_member_race = MemberRace(**member_race.dict())
    db.add(db_member_race)
    db.commit()
    db.refresh(db_member_race)
    return db_member_race

def get_member_race(db: Session, member_race_id: int):
    return db.query(MemberRace).filter(MemberRace.id == member_race_id).first()

def get_member_races_by_member_id(db: Session, member_id: int):
    return db.query(MemberRace).filter(MemberRace.memberId == member_id).all()

def delete_member_race(db: Session, member_race_id: int):
    db_member_race = get_member_race(db, member_race_id)
    if db_member_race:
        db.delete(db_member_race)
        db.commit()
    return db_member_race
