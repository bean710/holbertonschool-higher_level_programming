-- This script creates a table and adds 4 entries
-- Create the `second_table` table
CREATE TABLE IF NOT EXISTS second_table (
	id INT,
	name VARCHAR(256),
	score INT
);
-- Add John entry
INSERT INTO second_table VALUES (1, "John", 10);
-- Add Alex entry
INSERT INTO second_table VALUES (2, "Alex", 3);
-- Add Bob entry
INSERT INTO second_table VALUES (3, "Bob", 14);
-- Add George entry
INSERT INTO second_table VALUES (4, "George", 8);
