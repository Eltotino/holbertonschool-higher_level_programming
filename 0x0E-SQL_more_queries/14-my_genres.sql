-- Write a script that lists all shows contained in hbtn_0d_tvshows.
-- Select all genre from "DEXTER"

SELECT      genre.`name`
FROM        `tv_genres` AS genre
                INNER JOIN `tv_show_genres` AS shg
                    ON genre.`id` = shg.`genre_id`
                    INNER JOIN `tv_shows` AS sh
                        ON shg.`show_id` = sh.`id`
WHERE       sh.`title` = 'Dexter'
ORDER BY    genre.`name` ASC;
