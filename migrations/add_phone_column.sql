-- Migration script to add phone column to users table
-- Run this SQL script directly in your MySQL database

-- Check if phone column already exists
SELECT COUNT(*) as column_exists 
FROM INFORMATION_SCHEMA.COLUMNS 
WHERE TABLE_SCHEMA = DATABASE() 
AND TABLE_NAME = 'users' 
AND COLUMN_NAME = 'phone';

-- Add phone column if it doesn't exist
ALTER TABLE users 
ADD COLUMN phone VARCHAR(20) NULL 
AFTER password;

-- Verify the column was added
DESCRIBE users;
