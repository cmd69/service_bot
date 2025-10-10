"""
Database base configuration and utilities.
"""
import os
from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from decouple import config

# Database URL from environment
DATABASE_URL = config("DATABASE_URL", default="mysql+pymysql://subscription_user:subscription_pass@mysql:3306/subscription_bot")

# Debug: Print the database URL being used (without password for security)
import re
debug_url = re.sub(r':[^@]+@', ':***@', DATABASE_URL)
print(f"🔗 Using DATABASE_URL: {debug_url}")

# Create SQLAlchemy engine
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=300,
    echo=config("DEBUG", default=False, cast=bool)
)

# Create SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create Base class for models
Base = declarative_base()


def get_db() -> Generator[Session, None, None]:
    """
    Dependency to get database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db() -> None:
    """
    Initialize database tables.
    """
    # Import all models to ensure they are registered with Base
    from app.models import User, Plan, Subscription, Transaction, Wallet
    
    # Create all tables
    Base.metadata.create_all(bind=engine)
