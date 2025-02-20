from sqlalchemy.orm import Session
from model.member_address_model import MemberAddress
from model.member_address_schema import MemberAddressCreate

def create_member_address(db: Session, member_address_req: MemberAddressCreate):
    """Create a new member address record."""
    new_member_address = MemberAddress(**member_address_req.model_dump())
    db.add(new_member_address)
    db.commit()
    db.refresh(new_member_address)
    return new_member_address

def get_member_address(db: Session, member_address_id: int):
    """Retrieve a member address by ID."""
    return db.query(MemberAddress).filter(MemberAddress.id == member_address_id).first()

def get_all_member_addresses(db: Session):
    """Retrieve all member addresses."""
    return db.query(MemberAddress).all()

def update_member_address(db: Session, member_address_id: int, member_address_req: MemberAddressCreate):
    """Update an existing member address record."""
    member_address = db.query(MemberAddress).filter(MemberAddress.id == member_address_id).first()
    if not member_address:
        return None
    
    for key, value in member_address_req.model_dump().items():
        setattr(member_address, key, value)

    db.commit()
    db.refresh(member_address)
    return member_address

def delete_member_address(db: Session, member_address_id: int):
    """Delete a member address record."""
    member_address = db.query(MemberAddress).filter(MemberAddress.id == member_address_id).first()
    if not member_address:
        return None

    db.delete(member_address)
    db.commit()
    return member_address

def get_address_memberId(db: Session, member_id: int):
    return db.query(MemberAddress).filter(MemberAddress.memberId == member_id).first()