"""
Database session configuration.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from decouple import config

# Database URL from environment
DATABASE_URL = config("DATABASE_URL", default="mysql+pymysql://subscription_user:subscription_pass@mysql:3306/subscription_bot")

# Create SQLAlchemy engine
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=300,
    echo=config("DEBUG", default=False, cast=bool)
)

# Create SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """Get database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
