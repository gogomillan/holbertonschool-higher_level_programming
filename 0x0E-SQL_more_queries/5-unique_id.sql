-- Script that creates the table unique_id on a MySQL server.
-- Create table
CREATE TABLE IF NOT EXISTS unique_id
(
  id INT DEFAULT 1 UNIQUE,
  name VARCHAR(256)
) ENGINE=InnoDB;
