-- This script creates a user
-- Creates user user_0d_1
CREATE USER IF NOT EXISTS "user_0d_1"@"localhost" IDENTIFIED BY "user_0d_1_pwd";
-- Give all permissions to the new user
GRANT ALL PRIVILEGES ON * . * TO "user_0d_1"@"localhost";
