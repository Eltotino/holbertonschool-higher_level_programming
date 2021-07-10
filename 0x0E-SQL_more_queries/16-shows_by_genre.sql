-- Write a script that lists all shows contained in hbtn_0d_tvshows.
-- Select all shows and linked genres

SELECT      sh.`title`, genre.`name`
FROM        `tv_shows` AS sh
            LEFT JOIN `tv_show_genres` AS shg
                ON sh.`id` = shg.`show_id`
                LEFT JOIN `tv_genres` AS genre
                    ON shg.`genre_id` =  genre.`id`
ORDER BY    sh.`title` ASC,
            genre.`name` ASC;
