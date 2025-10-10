"""
Wallet service for managing crypto wallet addresses.
"""
import random
from typing import List, Optional
from decouple import config
from sqlalchemy.orm import Session

from app.models import Wallet, TransactionType
from app.database import get_db

# TODO Check if we actually need all this logic, we just want to setup wallet addresses on .env and get them added to sql
class WalletService:
    """Service for managing crypto wallets."""
    
    @staticmethod
    def load_wallets_from_env(db: Session) -> None:
        """
        Load wallet addresses from environment variables into database.
        """
        # Load TRX wallets
        trx_addresses = config("TRX_WALLETS", default="").split(",")
        trx_names = config("TRX_WALLET_NAMES", default="").split(",")
        
        for i, address in enumerate(trx_addresses):
            address = address.strip()
            if not address:
                continue
                
            # Check if wallet already exists
            existing_wallet = db.query(Wallet).filter(
                Wallet.address == address
            ).first()
            
            if not existing_wallet:
                name = trx_names[i].strip() if i < len(trx_names) and trx_names[i].strip() else f"TRX Wallet {i+1}"
                wallet = Wallet(
                    address=address,
                    network=TransactionType.CRYPTO_TRX,
                    name=name,
                    is_active=True
                )
                db.add(wallet)
        
        # Load BSC wallets
        bsc_addresses = config("BSC_WALLETS", default="").split(",")
        bsc_names = config("BSC_WALLET_NAMES", default="").split(",")
        
        for i, address in enumerate(bsc_addresses):
            address = address.strip()
            if not address:
                continue
                
            # Check if wallet already exists
            existing_wallet = db.query(Wallet).filter(
                Wallet.address == address
            ).first()
            
            if not existing_wallet:
                name = bsc_names[i].strip() if i < len(bsc_names) and bsc_names[i].strip() else f"BSC Wallet {i+1}"
                wallet = Wallet(
                    address=address,
                    network=TransactionType.CRYPTO_BSC,
                    name=name,
                    is_active=True
                )
                db.add(wallet)
        
        db.commit()
    
    @staticmethod
    def get_active_wallets(db: Session, network: TransactionType) -> List[Wallet]:
        """Get all active wallets for a specific network."""
        return db.query(Wallet).filter(
            Wallet.network == network,
            Wallet.is_active == True
        ).all()
    
    @staticmethod
    def get_random_wallet(db: Session, network: TransactionType) -> Optional[Wallet]:
        """Get a random active wallet for a specific network."""
        wallets = WalletService.get_active_wallets(db, network)
        return random.choice(wallets) if wallets else None
    
    @staticmethod
    def create_wallet(
        db: Session, 
        address: str, 
        network: TransactionType, 
        name: str = None,
        is_active: bool = True
    ) -> Wallet:
        """Create a new wallet."""
        wallet = Wallet(
            address=address,
            network=network,
            name=name or f"{network.value} Wallet",
            is_active=is_active
        )
        db.add(wallet)
        db.commit()
        db.refresh(wallet)
        return wallet
    
    @staticmethod
    def activate_wallet(db: Session, wallet_id: int) -> bool:
        """Activate a wallet."""
        wallet = db.query(Wallet).filter(Wallet.id == wallet_id).first()
        if wallet:
            wallet.activate()
            db.commit()
            return True
        return False
    
    @staticmethod
    def deactivate_wallet(db: Session, wallet_id: int) -> bool:
        """Deactivate a wallet."""
        wallet = db.query(Wallet).filter(Wallet.id == wallet_id).first()
        if wallet:
            wallet.deactivate()
            db.commit()
            return True
        return False
    
    @staticmethod
    def get_wallet_by_address(db: Session, address: str) -> Optional[Wallet]:
        """Get wallet by address."""
        return db.query(Wallet).filter(Wallet.address == address).first()
    
    @staticmethod
    def get_all_wallets(db: Session) -> List[Wallet]:
        """Get all wallets."""
        return db.query(Wallet).all()
    
    @staticmethod
    def get_wallets_by_network(db: Session, network: TransactionType) -> List[Wallet]:
        """Get all wallets for a specific network."""
        return db.query(Wallet).filter(Wallet.network == network).all()
    
    @staticmethod
    def initialize_wallets_from_env() -> None:
        """Initialize wallets from environment variables."""
        auto_create = config("AUTO_CREATE_WALLETS", default=True, cast=bool)
        if not auto_create:
            return
            
        db = next(get_db())
        try:
            WalletService.load_wallets_from_env(db)
            print("Wallets initialized from environment variables.")
        except Exception as e:
            print(f"Error initializing wallets: {e}")
        finally:
            db.close()
