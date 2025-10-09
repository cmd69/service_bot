"""
Wallet model for managing crypto wallet addresses.
"""
from typing import List, TYPE_CHECKING
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Enum, func, Index
from sqlalchemy.orm import relationship, Mapped

from app.database.base import Base
from .enums import TransactionType

if TYPE_CHECKING:
    from .transaction import Transaction


class Wallet(Base):
    """
    Wallet model for managing cryptocurrency wallet addresses.
    
    Stores wallet addresses for different blockchain networks (TRX, BSC)
    where transactions are received.
    """
    __tablename__ = "wallets"

    # Primary key
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    # Wallet details
    address = Column(String(100), unique=True, nullable=False, index=True)
    network = Column(
        Enum(TransactionType), 
        nullable=False,
        comment="Network type: CRYPTO_TRX or CRYPTO_BSC"
    )
    name = Column(String(100), nullable=True, comment="Friendly name for the wallet")
    
    # Status
    is_active = Column(Boolean, default=True, nullable=False)
    
    # Timestamps
    created_at = Column(DateTime, default=func.current_timestamp(), nullable=False)
    updated_at = Column(
        DateTime, 
        default=func.current_timestamp(), 
        onupdate=func.current_timestamp()
    )
    
    # Relationships
    transactions: Mapped[List["Transaction"]] = relationship(
        "Transaction", 
        back_populates="wallet",
        foreign_keys="Transaction.wallet_id"
    )
    
    # Indexes for performance
    __table_args__ = (
        Index('idx_wallets_network_active', 'network', 'is_active'),
    )
    
    def __repr__(self) -> str:
        return f"<Wallet(id={self.id}, address='{self.address}', network={self.network.value})>"
    
    @property
    def network_name(self) -> str:
        """Get friendly network name."""
        network_names = {
            TransactionType.CRYPTO_TRX: "TRON (TRX)",
            TransactionType.CRYPTO_BSC: "Binance Smart Chain (BSC)"
        }
        return network_names.get(self.network, self.network.value)
    
    @property
    def short_address(self) -> str:
        """Get shortened address for display."""
        if len(self.address) > 12:
            return f"{self.address[:6]}...{self.address[-6:]}"
        return self.address
    
    def activate(self) -> None:
        """Activate the wallet."""
        self.is_active = True
    
    def deactivate(self) -> None:
        """Deactivate the wallet."""
        self.is_active = False
    
    @classmethod
    def get_active_by_network(cls, session, network: TransactionType):
        """Get all active wallets for a specific network."""
        return session.query(cls).filter(
            cls.network == network,
            cls.is_active == True
        ).all()
    
    @classmethod
    def get_random_active_wallet(cls, session, network: TransactionType):
        """Get a random active wallet for a specific network."""
        import random
        wallets = cls.get_active_by_network(session, network)
        return random.choice(wallets) if wallets else None
