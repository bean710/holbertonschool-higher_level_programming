-- This script creates a database and a user
-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Switch to the new database
USE hbtn_0d_2;
-- Delete the user if it doesn't exist
DROP USER IF EXISTS user_0d_2@localhost;
-- Create the user
CREATE USER IF NOT EXISTS "user_0d_2"@"localhost" IDENTIFIED BY "user_0d_2_pwd";
-- Give the new user select permissions
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
-- Flush the privileges
FLUSH PRIVILEGES;
