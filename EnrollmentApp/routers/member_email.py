from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.db import get_db
from model.member_email import MEMBER_EMAIL
from model.member_email_schema import MemberEmailCreate

router = APIRouter()

### Create (Insert) a Member Email**
@router.post("/member_email/", response_model=MemberEmailCreate)
def create_member_email(email_data: MemberEmailCreate, db: Session = Depends(get_db)):
    new_email = MEMBER_EMAIL(**email_data.model_dump())
    db.add(new_email)
    db.commit()
    db.refresh(new_email)
    return new_email

### Read (Get) Email by ID**
@router.get("/member_email/{email_id}", response_model=MemberEmailCreate)
def get_member_email(email_id: int, db: Session = Depends(get_db)):
    email = db.query(MEMBER_EMAIL).filter(MEMBER_EMAIL.id == email_id).first()
    if not email:
        raise HTTPException(status_code=404, detail="Email not found")
    return email

### Read (Get) All Emails for a Member**
@router.get("/member/{member_id}/emails", response_model=list[MemberEmailCreate])
def get_member_emails(member_id: int, db: Session = Depends(get_db)):
    emails = db.query(MEMBER_EMAIL).filter(MEMBER_EMAIL.memberId == member_id).all()
    if not emails:
        raise HTTPException(status_code=404, detail="No emails found for this member")
    return emails


### Delete a Member Email**
@router.delete("/member_email/{email_id}")
def delete_member_email(email_id: int, db: Session = Depends(get_db)):
    email = db.query(MEMBER_EMAIL).filter(MEMBER_EMAIL.id == email_id).first()
    if not email:
        raise HTTPException(status_code=404, detail="Email not found")

    db.delete(email)
    db.commit()
    return {"message": "Email deleted successfully"}
