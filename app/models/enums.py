"""
Enums for database models.
"""
import enum


class SubscriptionStatus(enum.Enum):
    """Subscription status options."""
    ACTIVE = "active"
    EXPIRED = "expired"
    CANCELLED = "cancelled"
    PENDING = "pending"


class TransactionType(enum.Enum):
    """Transaction type options."""
    CRYPTO_TRX = "crypto_trx"
    CRYPTO_BSC = "crypto_bsc"
    BALANCE_CODE = "balance_code"


class TransactionStatus(enum.Enum):
    """Transaction status options."""
    PENDING = "pending"
    CONFIRMED = "confirmed"
    FAILED = "failed"
    REFUNDED = "refunded"
