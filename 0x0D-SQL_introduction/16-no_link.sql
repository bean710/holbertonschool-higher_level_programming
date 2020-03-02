-- This script lists all scores and names
-- Selects scores and names from the second_table and sorts them
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC
