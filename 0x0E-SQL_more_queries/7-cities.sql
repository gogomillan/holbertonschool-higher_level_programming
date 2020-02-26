-- Script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on a MySQL server.
-- Create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Create table
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities
(
  id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
  state_id INT NOT NULL,
  name VARCHAR(256) NOT NULL,
  FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states(id)
) ENGINE=InnoDB;
