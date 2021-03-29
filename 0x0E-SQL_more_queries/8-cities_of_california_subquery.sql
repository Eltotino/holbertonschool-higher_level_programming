-- Script that lists all the cities of California that are in hbtn_0d_usa database
-- Cities of California in hbtn_0d_usa database
SELECT id, name FROM cities
WHERE state_id  = (SELECT id FROM states WHERE name = 'California');
