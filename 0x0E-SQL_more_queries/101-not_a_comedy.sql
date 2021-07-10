-- Write a script that lists all shows contained in hbtn_0d_tvshows.
-- Select all shows not linked the comedy genre
SELECT DISTINCT sh.title
FROM tv_shows AS sh
LEFT JOIN tv_show_genres AS shg
ON sh.id = shg.show_id
LEFT JOIN tv_genres AS genre
ON shg.genre_id = genre.id
WHERE sh.title NOT IN (
    SELECT sh.title FROM tv_shows AS sh
    INNER JOIN tv_show_genres AS shg
    ON sh.id = shg.show_id
    INNER JOIN tv_genres AS genre
    ON shg.genre_id = genre.id
    WHERE genre.name = "Comedy"
)
ORDER BY sh.title ASC;
