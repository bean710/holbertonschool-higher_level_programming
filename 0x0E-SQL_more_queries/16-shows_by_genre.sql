-- This script lists all movies and their genre
SELECT tv_shows.title, tv_genres.name FROM tv_show_genres
INNER JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
ORDER BY tv_shows.title ASC;
