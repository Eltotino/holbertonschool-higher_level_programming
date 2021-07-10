-- Queries in MySQL server
-- Lists all genres by their rating
SELECT genre.name, SUM(ra.rate) AS rating
FROM tv_genres AS genre
INNER JOIN tv_show_genres AS shg
ON genre.id = shg.genre_id
INNER JOIN tv_shows AS sh
ON shg.show_id = sh.id
INNER JOIN tv_show_ratings AS ra
ON sh.id = ra.show_id
GROUP BY genre.name
ORDER BY rating DESC;
