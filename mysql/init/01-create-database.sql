-- Create database and user if they don't exist
-- This script runs automatically when MySQL container starts for the first time
-- Database name and user are read from environment variables

-- Create database using environment variable
CREATE DATABASE IF NOT EXISTS ${MYSQL_DATABASE} 
    CHARACTER SET utf8mb4 
    COLLATE utf8mb4_unicode_ci;

-- Use the database
USE ${MYSQL_DATABASE};

-- Grant privileges to the user specified in environment variables
GRANT ALL PRIVILEGES ON ${MYSQL_DATABASE}.* TO '${MYSQL_USER}'@'%';

-- Also grant privileges for any future database changes
-- This ensures the user has access to any database specified in .env
GRANT ALL PRIVILEGES ON *.* TO '${MYSQL_USER}'@'%' WITH GRANT OPTION;

FLUSH PRIVILEGES;

-- Create some sample data (optional)
-- This will be handled by the application, but we can add some basic plans here

-- Note: Tables will be created automatically by SQLAlchemy when the app starts
