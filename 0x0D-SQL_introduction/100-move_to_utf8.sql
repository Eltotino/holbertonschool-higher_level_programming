-- Script that converts hbtn_0c_0 to UTF-8
-- Converts database to UTF-8
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- Converts table to utf-8
ALTER TABLE hbtn_0c_0.first_table CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- Converts table to utf-8
ALTER TABLE hbtn_0c_0.first_table
MODIFY name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
