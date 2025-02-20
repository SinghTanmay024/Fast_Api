"""
API routes for managing addresses.
"""

from fastapi import APIRouter, Depends, Path
from sqlalchemy.orm import Session
from config.db import get_db
from model.address_schema import AddressRequest
from services.address_service import (
    get_all_addresses,
    get_address_by_id,
    create_address,
    update_address,
    delete_address,
)

router = APIRouter()

@router.get("/addresses", status_code=200)
async def get_all_addresses_route(db: Session = Depends(get_db)):  
    return get_all_addresses(db)  

@router.get("/addresses/{id}", status_code=200)
async def get_address(id: int = Path(gt=0), db: Session = Depends(get_db)):
    return get_address_by_id(db, id)

@router.post("/addresses", status_code=201)
async def create_new_address(address_req: AddressRequest, db: Session = Depends(get_db)):
    return create_address(db, address_req)

@router.put("/addresses/{id}", status_code=204)
async def update_existing_address(address_req: AddressRequest,db: Session = Depends(get_db),id: int = Path(gt=0)):
    return update_address(db, id, address_req)

@router.delete("/addresses/{id}", status_code=204)
async def remove_address(id: int, db: Session = Depends(get_db)):
    return delete_address(db, id)
