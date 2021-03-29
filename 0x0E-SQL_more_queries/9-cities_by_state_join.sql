-- Script that lists all the cities of California that are in hbtn_0d_usa database
-- Cities of California in hbtn_0d_usa database
SELECT cities.id, cities.name, states.name
FROM cities, states
ORDER BY cities.id ASC;
