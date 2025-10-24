#!/usr/bin/env python3
"""
Migration script to add phone column to users table.
Run this script to update the database schema.
"""

import sys
import os
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from sqlalchemy import create_engine, text
from decouple import config

def run_migration():
    """Add phone column to users table."""
    
    # Database connection
    db_host = config('DB_HOST', default='localhost')
    db_port = config('DB_PORT', default=3306, cast=int)
    db_user = config('DB_USER', default='root')
    db_password = config('DB_PASSWORD', default='')
    db_name = config('DB_NAME', default='jelly_admin')
    
    # Create database URL
    database_url = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    
    try:
        # Create engine
        engine = create_engine(database_url)
        
        with engine.connect() as connection:
            # Start transaction
            trans = connection.begin()
            
            try:
                # Check if phone column already exists
                result = connection.execute(text("""
                    SELECT COUNT(*) as count 
                    FROM INFORMATION_SCHEMA.COLUMNS 
                    WHERE TABLE_SCHEMA = :db_name 
                    AND TABLE_NAME = 'users' 
                    AND COLUMN_NAME = 'phone'
                """), {"db_name": db_name})
                
                count = result.fetchone()[0]
                
                if count > 0:
                    print("✅ Column 'phone' already exists in users table.")
                    trans.rollback()
                    return
                
                # Add phone column
                print("🔄 Adding phone column to users table...")
                connection.execute(text("""
                    ALTER TABLE users 
                    ADD COLUMN phone VARCHAR(20) NULL 
                    AFTER password
                """))
                
                # Commit transaction
                trans.commit()
                print("✅ Successfully added phone column to users table.")
                
            except Exception as e:
                trans.rollback()
                print(f"❌ Error during migration: {e}")
                raise
                
    except Exception as e:
        print(f"❌ Database connection error: {e}")
        print("Please check your database configuration in .env file.")
        sys.exit(1)

if __name__ == "__main__":
    print("🚀 Starting database migration...")
    print("📋 Adding phone column to users table")
    run_migration()
    print("🎉 Migration completed successfully!")
