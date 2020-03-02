-- This script lists the maximum temperature by state
-- This script gets max value for each state sorting by state name
SELECT state, MAX(value) AS "max_temp" FROM temperatures
GROUP BY state ORDER BY state ASC;
