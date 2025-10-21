"""
Database migration runner.
"""
import os
import sys
import importlib.util
from pathlib import Path

# Add the app directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..'))

from .. database.session import get_db


def run_migration(migration_file: str, downgrade: bool = False):
    """Run a specific migration."""
    migration_path = Path(__file__).parent / migration_file
    
    if not migration_path.exists():
        print(f"Migration file not found: {migration_path}")
        return False
    
    try:
        # Load migration module
        spec = importlib.util.spec_from_file_location("migration", migration_path)
        migration = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(migration)
        
        # Run migration
        if downgrade:
            migration.downgrade()
        else:
            migration.upgrade()
        
        return True
        
    except Exception as e:
        print(f"Error running migration {migration_file}: {e}")
        return False


def run_all_migrations():
    """Run all pending migrations."""
    migrations_dir = Path(__file__).parent
    migration_files = sorted([f for f in os.listdir(migrations_dir) 
                            if f.endswith('.py') and f != '__init__.py' and f != 'migrate.py'])
    
    print(f"Found {len(migration_files)} migration(s)")
    
    for migration_file in migration_files:
        print(f"\nRunning migration: {migration_file}")
        if not run_migration(migration_file):
            print(f"Migration {migration_file} failed. Stopping.")
            return False
    
    print("\nAll migrations completed successfully!")
    return True


def main():
    """Main migration runner."""
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "upgrade":
            run_all_migrations()
        elif command == "downgrade" and len(sys.argv) > 2:
            migration_file = sys.argv[2]
            run_migration(migration_file, downgrade=True)
        elif command == "run" and len(sys.argv) > 2:
            migration_file = sys.argv[2]
            run_migration(migration_file)
        else:
            print("Usage:")
            print("  python migrate.py upgrade                    # Run all migrations")
            print("  python migrate.py run <migration_file>      # Run specific migration")
            print("  python migrate.py downgrade <migration_file> # Rollback specific migration")
    else:
        print("Usage:")
        print("  python migrate.py upgrade                    # Run all migrations")
        print("  python migrate.py run <migration_file>      # Run specific migration")
        print("  python migrate.py downgrade <migration_file> # Rollback specific migration")


if __name__ == "__main__":
    main()
