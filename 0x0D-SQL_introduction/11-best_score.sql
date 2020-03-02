-- This script lists entries with a format
-- Selects all entries with scores above 10 and lists them in order of score
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
