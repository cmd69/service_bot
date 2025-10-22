"""
Subscription service for managing user subscriptions.
"""
from datetime import datetime, timedelta
from typing import List, Optional
from sqlalchemy.orm import Session

from ..models.subscription import Subscription
from ..models.plan import Plan
from ..models.user import User
from ..models.enums import SubscriptionStatus


class SubscriptionService:
    """Service for managing user subscriptions."""
    
    @staticmethod
    def create_subscription(
        db: Session,
        user_id: int,
        plan_id: int,
        start_date: datetime = None
    ) -> Optional[Subscription]:
        """Create a new subscription for a user."""
        user = db.query(User).filter(User.id == user_id).first()
        plan = db.query(Plan).filter(Plan.id == plan_id).first()
        
        if not user or not plan:
            return None
        
        if start_date is None:
            start_date = datetime.utcnow()
        
        end_date = plan.calculate_end_date(start_date)
        
        subscription = Subscription(
            user_id=user_id,
            plan_id=plan_id,
            start_date=start_date,
            end_date=end_date,
            status=SubscriptionStatus.ACTIVE
        )
        
        db.add(subscription)
        db.commit()
        db.refresh(subscription)
        return subscription
    
    @staticmethod
    def get_user_subscriptions(db: Session, user_id: int) -> List[Subscription]:
        """Get all subscriptions for a user."""
        return db.query(Subscription).filter(Subscription.user_id == user_id).all()
    
    @staticmethod
    def get_active_subscription(db: Session, user_id: int) -> Optional[Subscription]:
        """Get active subscription for a user."""
        return db.query(Subscription).filter(
            Subscription.user_id == user_id,
            Subscription.status == SubscriptionStatus.ACTIVE
        ).first()
    
    @staticmethod
    def get_all_plans(db: Session) -> List[Plan]:
        """Get all available plans."""
        return db.query(Plan).all()
    
    @staticmethod
    def cancel_subscription(db: Session, subscription_id: int) -> bool:
        """Cancel a subscription."""
        subscription = db.query(Subscription).filter(Subscription.id == subscription_id).first()
        if not subscription:
            return False
        
        subscription.cancel()
        db.commit()
        return True
    
    @staticmethod
    def expire_subscription(db: Session, subscription_id: int) -> bool:
        """Mark a subscription as expired."""
        subscription = db.query(Subscription).filter(Subscription.id == subscription_id).first()
        if not subscription:
            return False
        
        subscription.expire()
        db.commit()
        return True
    
    @staticmethod
    def get_subscription_by_id(db: Session, subscription_id: int) -> Optional[Subscription]:
        """Get subscription by ID."""
        return db.query(Subscription).filter(Subscription.id == subscription_id).first()
    
    @staticmethod
    def get_all_subscriptions(db: Session) -> List[Subscription]:
        """Get all subscriptions."""
        return db.query(Subscription).all()
    
    @staticmethod
    def get_active_subscriptions(db: Session) -> List[Subscription]:
        """Get all active subscriptions."""
        return db.query(Subscription).filter(
            Subscription.status == SubscriptionStatus.ACTIVE
        ).all()
    
    @staticmethod
    def get_expired_subscriptions(db: Session) -> List[Subscription]:
        """Get all expired subscriptions."""
        return db.query(Subscription).filter(
            Subscription.status == SubscriptionStatus.EXPIRED
        ).all()
    
    @staticmethod
    def get_cancelled_subscriptions(db: Session) -> List[Subscription]:
        """Get all cancelled subscriptions."""
        return db.query(Subscription).filter(
            Subscription.status == SubscriptionStatus.CANCELLED
        ).all()
    
    @staticmethod
    def update_subscription_status(
        db: Session, 
        subscription_id: int, 
        status: SubscriptionStatus
    ) -> bool:
        """Update subscription status."""
        subscription = db.query(Subscription).filter(Subscription.id == subscription_id).first()
        if not subscription:
            return False
        
        subscription.status = status
        db.commit()
        return True
    
    @staticmethod
    def update_subscription_dates(
        db: Session,
        subscription_id: int,
        start_date: datetime,
        end_date: datetime
    ) -> bool:
        """Update subscription start and end dates."""
        subscription = db.query(Subscription).filter(Subscription.id == subscription_id).first()
        if not subscription:
            return False
        
        subscription.start_date = start_date
        subscription.end_date = end_date
        db.commit()
        return True
    
    @staticmethod
    def delete_subscription(db: Session, subscription_id: int) -> bool:
        """Delete a subscription."""
        subscription = db.query(Subscription).filter(Subscription.id == subscription_id).first()
        if not subscription:
            return False
        
        db.delete(subscription)
        db.commit()
        return True
