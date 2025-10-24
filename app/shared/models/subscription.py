"""
Subscription model for user subscriptions to plans.
"""
from datetime import datetime
from typing import List, TYPE_CHECKING
from sqlalchemy import Column, Integer, ForeignKey, DateTime, Enum, func, Index
from sqlalchemy.orm import relationship, Mapped

from .. database.base import Base
from .enums import SubscriptionStatus

if TYPE_CHECKING:
    from .user import User
    from .plan import Plan
    from .transaction import Transaction


class Subscription(Base):
    """
    Subscription model tracking user subscriptions to plans.
    
    A user can have multiple (historical), but only one active at a time.
    """
    __tablename__ = "subscriptions"

    # Primary key
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    # Foreign keys
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    plan_id = Column(Integer, ForeignKey("plans.id", ondelete="RESTRICT"), nullable=False)
    
    # Subscription period
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    
    # Status
    status = Column(
        Enum(SubscriptionStatus), 
        default=SubscriptionStatus.ACTIVE, 
        nullable=False
    )
    
    # Timestamps
    created_at = Column(DateTime, default=func.current_timestamp(), nullable=False)
    
    # Relationships
    user: Mapped["User"] = relationship("User", back_populates="subscriptions")
    plan: Mapped["Plan"] = relationship("Plan", back_populates="subscriptions")
    transactions: Mapped[List["Transaction"]] = relationship(
        "Transaction", 
        back_populates="subscription"
    )
    
    # Indexes for performance
    __table_args__ = (
        Index('idx_subscriptions_user_status', 'user_id', 'status'),
        Index('idx_subscriptions_dates', 'start_date', 'end_date'),
    )
    
    def __repr__(self) -> str:
        return f"<Subscription(id={self.id}, user_id={self.user_id}, plan_id={self.plan_id}, status={self.status.value})>"
    
    @property
    def is_active(self) -> bool:
        """Check if subscription is currently active."""
        now = datetime.utcnow()
        return (
            self.status == SubscriptionStatus.ACTIVE and 
            self.start_date <= now <= self.end_date
        )
    
    @property
    def is_expired(self) -> bool:
        """Check if subscription has expired."""
        return datetime.utcnow() > self.end_date
    
    @property
    def days_remaining(self) -> int:
        """
        Get number of days remaining in subscription.
        Returns positive number if active, negative if expired (to show how many days ago it expired).
        """
        return (self.end_date - datetime.utcnow()).days
    
    def expire(self) -> None:
        """Mark subscription as expired."""
        self.status = SubscriptionStatus.EXPIRED
    
    def cancel(self) -> None:
        """Cancel the subscription."""
        self.status = SubscriptionStatus.CANCELLED
