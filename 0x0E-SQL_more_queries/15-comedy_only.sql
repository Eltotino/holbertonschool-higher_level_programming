-- Write a script that lists all shows contained in hbtn_0d_tvshows.
-- Select all Comedy shows
SELECT title FROM tv_show_genres tsg
INNER JOIN tv_genres tg
ON tsg.genre_id = tg.id
   INNER JOIN tv_shows tvs
   ON tsg.show_id = tvs.id
WHERE name = 'Comedy'
ORDER BY title ASC;
