-- Queries in MySQL server
-- Select rating by shows
SELECT sh.title, sum(r.rate) AS rating
FROM tv_shows AS sh
INNER JOIN tv_show_ratings AS r
ON sh.id = r.show_id
GROUP BY sh.title
ORDER BY rating DESC;
