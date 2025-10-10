"""
User model for the subscription system.
"""
from datetime import datetime
from typing import List, TYPE_CHECKING
from sqlalchemy import Column, Integer, BigInteger, String, Boolean, DateTime, func
from sqlalchemy.orm import relationship, Mapped

from app.database.base import Base

if TYPE_CHECKING:
    from .subscription import Subscription
    from .transaction import Transaction


class User(Base):
    """
    User model representing users in the subscription system.
    
    Users can be created either through Telegram bot (with chat_id) or 
    through the admin panel (without chat_id). Stores basic data including
    credentials and role/status flags.
    """
    __tablename__ = "users"

    # Primary key
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    # Telegram integration (optional - if None, user was created outside Telegram)
    chat_id = Column(BigInteger, unique=True, nullable=True, index=True)
    
    # User credentials
    name = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)  # Should be hashed
    
    # Role and status flags
    is_admin = Column(Boolean, default=False, nullable=False)
    is_member = Column(Boolean, default=False, nullable=False)
    
    # Timestamps
    created_at = Column(DateTime, default=func.current_timestamp(), nullable=False)
    updated_at = Column(
        DateTime, 
        default=func.current_timestamp(), 
        onupdate=func.current_timestamp()
    )
    
    # Relationships
    subscriptions: Mapped[List["Subscription"]] = relationship(
        "Subscription", 
        back_populates="user",
        cascade="all, delete-orphan"
    )
    
    transactions: Mapped[List["Transaction"]] = relationship(
        "Transaction", 
        back_populates="user",
        cascade="all, delete-orphan"
    )
    
    def __repr__(self) -> str:
        chat_info = f"chat_id={self.chat_id}" if self.chat_id else "no_telegram"
        return f"<User(id={self.id}, {chat_info}, name='{self.name}')>"
    
    @property
    def active_subscription(self) -> "Subscription":
        """Get the current active subscription for this user."""
        from .enums import SubscriptionStatus
        return next(
            (sub for sub in self.subscriptions 
             if sub.status == SubscriptionStatus.ACTIVE and sub.end_date > datetime.utcnow()), 
            None
        )
    
    def has_active_subscription(self) -> bool:
        """Check if user has an active subscription."""
        return self.active_subscription is not None
    
    def is_telegram_user(self) -> bool:
        """Check if user was created through Telegram (has chat_id)."""
        return self.chat_id is not None
