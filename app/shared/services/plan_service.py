"""
Plan service for managing subscription plans.
"""
import json
from decimal import Decimal
from typing import List, Dict, Any
from decouple import config
from sqlalchemy.orm import Session

from .. models.plan import Plan
from .. database.session import get_db


class PlanService:
    """Service for managing subscription plans."""
    
    @staticmethod
    def load_plans_from_env(db: Session) -> None:
        """Load plans from environment variables into database."""
        plans_data = None
        
        # Try to load from JSON file first
        plans_config_file = config("PLANS_CONFIG_FILE", default="")
        if plans_config_file:
            # If no path is specified, look in the texts directory
            if not plans_config_file.startswith('/') and not plans_config_file.startswith('./'):
                plans_config_file = f"/app/texts/{plans_config_file}"
            
            try:
                with open(plans_config_file, 'r', encoding='utf-8') as f:
                    plans_data = json.load(f)
                print(f"Loaded plans from file: {plans_config_file}")
            except (FileNotFoundError, json.JSONDecodeError) as e:
                print(f"Error loading plans from file {plans_config_file}: {e}")
        
        # Fallback to inline JSON config
        if not plans_data:
            plans_config = config("PLANS_CONFIG", default="{}")
            try:
                plans_data = json.loads(plans_config)
                if plans_data:
                    print("Loaded plans from inline JSON config")
            except json.JSONDecodeError as e:
                print(f"Error parsing PLANS_CONFIG JSON: {e}")
                return
        
        if not plans_data:
            print("No plans configuration found in PLANS_CONFIG or PLANS_CONFIG_FILE.")
            return
        
        created_count = 0
        for plan_key, plan_data in plans_data.items():
            # Check if plan already exists
            existing_plan = db.query(Plan).filter(Plan.name == plan_data["name"]).first()
            if existing_plan:
                print(f"Plan '{plan_data['name']}' already exists, skipping.")
                continue
            
            # Create new plan
            plan = Plan(
                name=plan_data["name"],
                duration_days=plan_data["duration_days"],
                number_accounts=plan_data["number_accounts"],
                price=Decimal(str(plan_data["price"])),
                description=plan_data.get("description", "")
            )
            
            db.add(plan)
            created_count += 1
        
        if created_count > 0:
            db.commit()
            print(f"Created {created_count} plans from environment configuration.")
        else:
            print("No new plans created.")
    
    @staticmethod
    def get_all_plans(db: Session) -> List[Plan]:
        """Get all available plans."""
        return db.query(Plan).all()
    
    @staticmethod
    def get_plan_by_id(db: Session, plan_id: int) -> Plan:
        """Get plan by ID."""
        return db.query(Plan).filter(Plan.id == plan_id).first()
    
    @staticmethod
    def get_plan_by_name(db: Session, name: str) -> Plan:
        """Get plan by name."""
        return db.query(Plan).filter(Plan.name == name).first()
    
    @staticmethod
    def create_plan(
        db: Session,
        name: str,
        duration_days: int,
        number_accounts: int,
        price: Decimal,
        description: str = ""
    ) -> Plan:
        """Create a new plan."""
        plan = Plan(
            name=name,
            duration_days=duration_days,
            number_accounts=number_accounts,
            price=price,
            description=description
        )
        
        db.add(plan)
        db.commit()
        db.refresh(plan)
        return plan
    
    @staticmethod
    def initialize_plans_from_env() -> None:
        """Initialize plans from environment variables."""
        auto_create = config("AUTO_CREATE_PLANS", default=True, cast=bool)
        if not auto_create:
            return
            
        db = next(get_db())
        try:
            PlanService.load_plans_from_env(db)
        except Exception as e:
            print(f"Error creating plans: {e}")
        finally:
            db.close()
    
    @staticmethod
    def get_plans_summary(db: Session) -> List[Dict[str, Any]]:
        """Get a summary of all plans for display."""
        plans = PlanService.get_all_plans(db)
        return [
            {
                "id": plan.id,
                "name": plan.name,
                "price": str(plan.price),
                "duration_days": plan.duration_days,
                "number_accounts": plan.number_accounts,
                "description": plan.description
            }
            for plan in plans
        ]
