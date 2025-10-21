"""
Plan model for subscription plans.
"""
from decimal import Decimal
from datetime import datetime
from typing import List, TYPE_CHECKING
from sqlalchemy import Column, Integer, String, Text, DECIMAL, DateTime, func, CheckConstraint
from sqlalchemy.orm import relationship, Mapped

from .. database.base import Base

if TYPE_CHECKING:
    from .subscription import Subscription


class Plan(Base):
    """
    Plan model defining available subscription plans.
    
    Contains duration, number of accounts allowed, and pricing information.
    """
    __tablename__ = "plans"

    # Primary key
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    # Plan details
    name = Column(String(100), nullable=False)
    duration_days = Column(Integer, nullable=False)
    number_accounts = Column(Integer, nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)
    description = Column(Text, nullable=True)
    
    # Timestamps
    created_at = Column(DateTime, default=func.current_timestamp(), nullable=False)
    
    # Relationships
    subscriptions: Mapped[List["Subscription"]] = relationship(
        "Subscription", 
        back_populates="plan"
    )
    
    # Constraints
    __table_args__ = (
        CheckConstraint('duration_days > 0', name='check_duration_positive'),
        CheckConstraint('number_accounts > 0', name='check_accounts_positive'),
        CheckConstraint('price >= 0', name='check_price_non_negative'),
    )
    
    def __repr__(self) -> str:
        return f"<Plan(id={self.id}, name='{self.name}', duration_days={self.duration_days})>"
    
    @property
    def price_formatted(self) -> str:
        """Get formatted price string."""
        return f"{self.price:.2f}€"
    
    def calculate_end_date(self, start_date: datetime) -> datetime:
        """Calculate end date based on plan duration."""
        from datetime import timedelta
        return start_date + timedelta(days=self.duration_days)
