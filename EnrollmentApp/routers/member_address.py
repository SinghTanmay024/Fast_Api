from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.db import get_db
from model.member_address_model import MemberAddress
from model.address_models import Address
from model.member_address_schema import MemberAddressCreate
from services.address_service import (
    get_address_by_id
)
from services.member_address_service import (
    create_member_address, get_member_address, get_all_member_addresses,
    update_member_address, delete_member_address,
    get_address_memberId
)

router = APIRouter()

@router.post("/member_addresses/")
def create_member_address_route(member_address_req: MemberAddressCreate, db: Session = Depends(get_db)):
    """API to create a new member address."""
    return create_member_address(db, member_address_req)

@router.get("/member_addresses/{member_address_id}")
def get_member_address_route(member_address_id: int, db: Session = Depends(get_db)):
    """API to retrieve a member address by ID."""
    member_address = get_member_address(db, member_address_id)
    if not member_address:
        raise HTTPException(status_code=404, detail="Member address not found")
    return member_address

@router.get("/member_addresses/")
def get_all_member_addresses_route(db: Session = Depends(get_db)):
    """API to retrieve all member addresses."""
    return get_all_member_addresses(db)

@router.put("/member_addresses/{member_address_id}")
def update_member_address_route(member_address_id: int, member_address_req: MemberAddressCreate, db: Session = Depends(get_db)):
    """API to update an existing member address."""
    updated_member_address = update_member_address(db, member_address_id, member_address_req)
    if not updated_member_address:
        raise HTTPException(status_code=404, detail="Member address not found")
    return updated_member_address

@router.delete("/member_addresses/{member_address_id}")
def delete_member_address_route(member_address_id: int, db: Session = Depends(get_db)):
    """API to delete a member address."""
    deleted_member_address = delete_member_address(db, member_address_id)
    if not deleted_member_address:
        raise HTTPException(status_code=404, detail="Member address not found")
    return {"message": "Member address deleted successfully"}

@router.get("/member/{member_id}/address")
def get_address_by_member_id(member_id: int, db: Session = Depends(get_db)):
    """API to retrieve a member's address using memberId."""

    # Step 1: Find the MEMBER_ADDRESS record using member_id
    member_address = get_address_memberId(db,member_id)

    if not member_address:
        raise HTTPException(status_code=404, detail="No address found for this member")

    # Step 2: Get the corresponding address from the ADDRESS table
    address = get_address_by_id(db,member_address.addressId)
    # address = db.query(Address).filter(Address.id == member_address.addressId).first()

    if not address:
        raise HTTPException(status_code=404, detail="Address details not found")

    return address  # Return the full address details
