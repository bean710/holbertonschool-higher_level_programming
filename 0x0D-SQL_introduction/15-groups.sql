-- This script lists the number of records with the same score
-- Selects scores and count and then groups by count
SELECT score, COUNT(*) AS "number" FROM second_table 
GROUP BY score ORDER BY number;
