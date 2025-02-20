"""
Service layer for handling business logic related to address operations.
"""

from sqlalchemy.orm import Session
from model.address_models import Address
from model.address_schema import AddressRequest
from fastapi import HTTPException

def get_all_addresses(db: Session):
    """Fetch all addresses from the database."""
    return db.query(Address).all()

def get_address_by_id(db: Session, address_id: int):
    """Fetch a specific address by ID."""
    address = db.query(Address).filter(Address.id == address_id).first()
    if address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    return address

def create_address(db: Session, address_req: AddressRequest):
    """Create a new address record."""
    address_model = Address(**address_req.model_dump())
    db.add(address_model)
    db.commit()
    db.refresh(address_model)
    return address_model

def update_address(db: Session, address_id: int, address_req: AddressRequest):
    """Update an existing address record."""
    address_model = db.query(Address).filter(Address.id == address_id).first()
    if address_model is None:
        raise HTTPException(status_code=404, detail="Address not found")

    for key, value in address_req.model_dump().items():
        setattr(address_model, key, value)

    db.commit()
    db.refresh(address_model)
    return address_model

def delete_address(db: Session, address_id: int):
    """Delete an address record."""
    address_model = db.query(Address).filter(Address.id == address_id).first()
    if address_model is None:
        raise HTTPException(status_code=404, detail="Address not found")

    db.delete(address_model)
    db.commit()
