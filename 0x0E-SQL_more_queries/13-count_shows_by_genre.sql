-- This script gets the number of shows by genre
-- Select the name and number of shows
SELECT name, COUNT(show_id) AS number_of_shows FROM tv_genres
-- Join the genres table based on id
INNER JOIN tv_show_genres ON genre_id = id
-- Group the genres together and sort by number of shows
GROUP BY name ORDER BY number_of_shows DESC;
