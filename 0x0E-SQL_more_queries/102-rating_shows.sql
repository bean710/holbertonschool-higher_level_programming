-- This script lists shows in order of rating
SELECT tv_shows.title, SUM(tv_show_ratings.rate) AS rating FROM tv_shows
INNER JOIN tv_show_ratings ON tv_show_ratings.show_id = tv_shows.id
GROUP BY tv_show_ratings.show_id
ORDER BY rating DESC;
