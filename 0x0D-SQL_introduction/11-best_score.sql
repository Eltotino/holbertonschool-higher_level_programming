-- Script that lists all records of the table second_table from hbtn_0c_0 in MySQL server
-- Lists all records from second_table ordered by score >= 12 in descending order
SELECT score, name FROM second_table
WHERE score >= 10 ORDER BY score DESC;
