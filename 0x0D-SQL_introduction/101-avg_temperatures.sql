-- This script gets the average temperature by city
-- Get averages by city
SELECT city, AVG(value) AS "avg_temp" FROM temperatures
GROUP BY city ORDER BY avg_temp DESC;
