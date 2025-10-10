"""
Transaction model for logging subscription transactions.
"""
from decimal import Decimal
from typing import Optional, Dict, Any, TYPE_CHECKING
from sqlalchemy import Column, Integer, ForeignKey, String, DECIMAL, DateTime, Enum, JSON, func, Index
from sqlalchemy.orm import relationship, Mapped

from app.database.base import Base
from .enums import TransactionType, TransactionStatus

if TYPE_CHECKING:
    from .user import User
    from .subscription import Subscription
    from .wallet import Wallet


class Transaction(Base):
    """
    Transaction model for logging transactions for acquiring subscriptions.
    
    Supports types: crypto (TRX/BSC) or balance code (mobile + code).
    Linked to a specific subscription.
    """
    __tablename__ = "transactions"

    # Primary key
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    # Foreign keys
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    subscription_id = Column(
        Integer, 
        ForeignKey("subscriptions.id", ondelete="SET NULL"), 
        nullable=True
    )
    wallet_id = Column(
        Integer, 
        ForeignKey("wallets.id", ondelete="SET NULL"), 
        nullable=True,
        comment="Wallet used for crypto transactions"
    )
    
    # Transaction details
    type = Column(Enum(TransactionType), nullable=False)
    amount = Column(DECIMAL(10, 2), nullable=False)
    status = Column(
        Enum(TransactionStatus), 
        default=TransactionStatus.PENDING, 
        nullable=False
    )
    
    # Timestamps
    transaction_date = Column(DateTime, default=func.current_timestamp(), nullable=False)
    
    # Crypto transaction fields
    transaction_hash = Column(String(255), nullable=True)
    wallet_address = Column(String(100), nullable=True)
    
    # Balance code fields
    mobile = Column(String(20), nullable=True)
    code = Column(String(50), nullable=True)
    
    # Flexible field for additional data
    details = Column(JSON, nullable=True)
    
    # Relationships
    user: Mapped["User"] = relationship("User", back_populates="transactions")
    subscription: Mapped[Optional["Subscription"]] = relationship("Subscription", back_populates="transactions")
    wallet: Mapped[Optional["Wallet"]] = relationship("Wallet", back_populates="transactions")
    
    # Indexes for performance
    __table_args__ = (
        Index('idx_transactions_user_status', 'user_id', 'status'),
        Index('idx_transactions_type_status', 'type', 'status'),
        Index('idx_transactions_hash', 'transaction_hash'),
    )
    
    def __repr__(self) -> str:
        return f"<Transaction(id={self.id}, user_id={self.user_id}, type={self.type.value}, status={self.status.value})>"
    
    @property
    def is_crypto_transaction(self) -> bool:
        """Check if this is a crypto transaction."""
        return self.type in [TransactionType.CRYPTO_TRX, TransactionType.CRYPTO_BSC]
    
    @property
    def is_balance_code_transaction(self) -> bool:
        """Check if this is a balance code transaction."""
        return self.type == TransactionType.BALANCE_CODE
    
    @property
    def amount_formatted(self) -> str:
        """Get formatted amount string."""
        return f"${self.amount:.2f}"
    
    def confirm(self) -> None:
        """Mark transaction as confirmed."""
        self.status = TransactionStatus.CONFIRMED
    
    def fail(self, reason: Optional[str] = None) -> None:
        """Mark transaction as failed."""
        self.status = TransactionStatus.FAILED
        if reason and self.details:
            self.details = {**self.details, "failure_reason": reason}
        elif reason:
            self.details = {"failure_reason": reason}
    
    def refund(self, reason: Optional[str] = None) -> None:
        """Mark transaction as refunded."""
        self.status = TransactionStatus.REFUNDED
        if reason and self.details:
            self.details = {**self.details, "refund_reason": reason}
        elif reason:
            self.details = {"refund_reason": reason}
    
    def add_crypto_details(self, transaction_hash: str, wallet_address: str = None, **kwargs) -> None:
        """Add crypto transaction details."""
        self.transaction_hash = transaction_hash
        # If wallet_address is provided, store it for backward compatibility
        if wallet_address:
            self.wallet_address = wallet_address
        # If wallet is assigned, use its address
        elif self.wallet:
            self.wallet_address = self.wallet.address
        if kwargs:
            self.details = {**(self.details or {}), **kwargs}
    
    def add_balance_code_details(self, mobile: str, code: str, **kwargs) -> None:
        """Add balance code transaction details."""
        self.mobile = mobile
        self.code = code
        if kwargs:
            self.details = {**(self.details or {}), **kwargs}
