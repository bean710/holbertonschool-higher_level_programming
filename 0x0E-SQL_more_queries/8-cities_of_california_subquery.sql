-- This script gets a list of cities from california
SELECT id, name FROM cities WHERE state_id =
	(SELECT id FROM states WHERE name = "California");
