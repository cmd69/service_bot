"""
User service for managing users and admin operations.
"""
import hashlib
import secrets
from typing import Optional
from decouple import config
from sqlalchemy.orm import Session

from app.models import User
from app.database import get_db


class UserService:
    """Service for managing users."""
    
    @staticmethod
    def hash_password(password: str) -> str:
        """Hash a password using SHA-256 with salt."""
        salt = secrets.token_hex(16)
        password_hash = hashlib.sha256((password + salt).encode()).hexdigest()
        return f"{salt}:{password_hash}"
    
    @staticmethod
    def verify_password(password: str, hashed_password: str) -> bool:
        """Verify a password against its hash."""
        try:
            salt, password_hash = hashed_password.split(":")
            return hashlib.sha256((password + salt).encode()).hexdigest() == password_hash
        except ValueError:
            return False
    
    @staticmethod
    def generate_credentials() -> tuple[str, str]:
        """Generate random username and password."""
        username = f"user_{secrets.token_hex(8)}"
        password = secrets.token_hex(12)
        return username, password
    
    @staticmethod
    def create_user(
        db: Session,
        chat_id: int,
        name: str = None,
        password: str = None,
        is_admin: bool = False,
        is_member: bool = False
    ) -> User:
        """Create a new user."""
        # Generate credentials if not provided
        if not name or not password:
            generated_name, generated_password = UserService.generate_credentials()
            name = name or generated_name
            password = password or generated_password
        
        # Hash the password
        hashed_password = UserService.hash_password(password)
        
        user = User(
            chat_id=chat_id,
            name=name,
            password=hashed_password,
            is_admin=is_admin,
            is_member=is_member
        )
        
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    
    @staticmethod
    def get_user_by_chat_id(db: Session, chat_id: int) -> Optional[User]:
        """Get user by Telegram chat ID."""
        return db.query(User).filter(User.chat_id == chat_id).first()
    
    @staticmethod
    def get_admin_user(db: Session) -> Optional[User]:
        """Get the admin user."""
        return db.query(User).filter(User.is_admin == True).first()
    
    @staticmethod
    def create_admin_user(db: Session) -> Optional[User]:
        """Create admin user from environment variables."""
        admin_chat_id = config("ADMIN_CHAT_ID", default=None, cast=int)
        admin_username = config("ADMIN_USERNAME", default="admin")
        admin_password = config("ADMIN_PASSWORD", default="admin123")
        
        if not admin_chat_id:
            print("ADMIN_CHAT_ID not configured, skipping admin user creation.")
            return None
        
        # Check if admin already exists
        existing_admin = UserService.get_admin_user(db)
        if existing_admin:
            print("Admin user already exists, skipping creation.")
            return existing_admin
        
        # Check if user with this chat_id already exists
        existing_user = UserService.get_user_by_chat_id(db, admin_chat_id)
        if existing_user:
            # Update existing user to be admin
            existing_user.is_admin = True
            existing_user.name = admin_username
            existing_user.password = UserService.hash_password(admin_password)
            db.commit()
            db.refresh(existing_user)
            print(f"Updated existing user to admin: {admin_username}")
            return existing_user
        
        # Create new admin user
        admin_user = UserService.create_user(
            db=db,
            chat_id=admin_chat_id,
            name=admin_username,
            password=admin_password,
            is_admin=True,
            is_member=True
        )
        
        print(f"Created admin user: {admin_username} (Chat ID: {admin_chat_id})")
        return admin_user
    
    @staticmethod
    def initialize_admin_from_env() -> None:
        """Initialize admin user from environment variables."""
        auto_create = config("AUTO_CREATE_ADMIN", default=True, cast=bool)
        if not auto_create:
            return
            
        db = next(get_db())
        try:
            UserService.create_admin_user(db)
        except Exception as e:
            print(f"Error creating admin user: {e}")
        finally:
            db.close()
