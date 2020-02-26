-- Script that creates the table id_not_null on a MySQL server.
-- Create table
CREATE TABLE IF NOT EXISTS id_not_null (
  id INT DEFAULT 1,
  name VARCHAR(256)
) ENGINE=InnoDB;
