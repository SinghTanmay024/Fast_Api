"""
Main entry point for the FastAPI application.
"""

from fastapi import FastAPI
from config import db
from config.db import engine
from routers import members, address, member_address, member_email
from routers import member_race

app = FastAPI()

db.Base.metadata.create_all(bind=engine)

app.include_router(members.router, tags=["Members"])
app.include_router(address.router, tags=["Addresses"])
app.include_router(member_address.router, tags=["Member Addresses"])
app.include_router(member_email.router, tags=["Member Emails"])
app.include_router(member_race.router, tags=["Member Races"])