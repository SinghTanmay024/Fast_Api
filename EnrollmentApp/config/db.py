"""
Database configuration and session setup for the FastAPI application.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:root@localhost:3306/Enrollment"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def create_tables():
    """Creates all database tables based on the defined SQLAlchemy models."""
    Base.metadata.create_all(bind=engine)

def get_db():
    """Dependency function to get the database session."""
    db = SessionLocal()
    try:
        yield db  # Provides a database session
    finally:
        db.close()  # Ensures the session is closed after use