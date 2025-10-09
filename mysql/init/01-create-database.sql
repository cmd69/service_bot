-- Create database and user if they don't exist
-- This script runs automatically when MySQL container starts for the first time

-- Create database
CREATE DATABASE IF NOT EXISTS subscription_bot 
    CHARACTER SET utf8mb4 
    COLLATE utf8mb4_unicode_ci;

-- Use the database
USE subscription_bot;

-- Grant privileges to the subscription_user
GRANT ALL PRIVILEGES ON subscription_bot.* TO 'subscription_user'@'%';
FLUSH PRIVILEGES;

-- Create some sample data (optional)
-- This will be handled by the application, but we can add some basic plans here

-- Note: Tables will be created automatically by SQLAlchemy when the app starts
