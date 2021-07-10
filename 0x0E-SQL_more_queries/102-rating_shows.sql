-- Queries in MySQL server
-- Select rating by shows
SELECT sh.title, sum(ra.rate) AS rating
FROM tv_shows AS sh
INNER JOIN tv_show_ratings AS ra
ON sh.id = ra.show_id
GROUP BY sh.title
ORDER BY rating DESC;
