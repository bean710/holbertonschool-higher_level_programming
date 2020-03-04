-- This script gets a list of cities from california
-- Get a list of cities in a certain state
SELECT id, name FROM cities WHERE state_id =
-- Get the state_id of California
	(SELECT id FROM states WHERE name = "California");
