-- Write a script that lists all shows contained in hbtn_0d_tvshows.
-- tv shows in hbtn_0d_tvshows database
SELECT title, genre_id FROM tv_shows,
LEFT JOIN tv_shows_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY 
	title ASC,
	genre_id ASC;
