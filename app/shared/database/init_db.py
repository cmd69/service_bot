"""
Database initialization script.
"""
from app.database.base import init_db
from app.services import WalletService, UserService, PlanService


def initialize_wallets():
    """Initialize wallets from environment variables."""
    print("Initializing wallets from environment...")
    try:
        WalletService.initialize_wallets_from_env()
        print("Wallets initialized successfully.")
    except Exception as e:
        print(f"Error initializing wallets: {e}")


def initialize_plans():
    """Initialize plans from environment variables."""
    print("Initializing plans from environment...")
    try:
        PlanService.initialize_plans_from_env()
        print("Plans initialized successfully.")
    except Exception as e:
        print(f"Error initializing plans: {e}")


def initialize_admin():
    """Initialize admin user from environment variables."""
    print("Initializing admin user from environment...")
    try:
        UserService.initialize_admin_from_env()
        print("Admin user initialized successfully.")
    except Exception as e:
        print(f"Error initializing admin user: {e}")


def initialize_database():
    """Initialize the database with tables and configuration from environment."""
    print("Initializing database...")
    
    # Create all tables
    init_db()
    print("Database tables created successfully.")
    
    # Initialize plans from environment
    initialize_plans()
    
    # Initialize wallets from environment
    initialize_wallets()
    
    # Initialize admin user from environment
    initialize_admin()
    
    print("Database initialization completed.")


if __name__ == "__main__":
    initialize_database()
