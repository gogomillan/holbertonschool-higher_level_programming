# Chalenge Python - Object-relational mapping

## Background Context
This project is about link two amazing worlds: Databases and Python!  
In the first part, the module MySQLdb to connect to a MySQL database and execute your SQL queries.  
In the second part, the module SQLAlchemy (dont ask me how to pronounce it) an Object Relational Mapper (ORM).   

## Topics
- Why Python programming is awesome. :))
- How to connect to a MySQL database from a Python script
- How to SELECT rows in a MySQL table from a Python script
- How to INSERT rows in a MySQL table from a Python script
- What ORM means
- How to map a Python Class to a MySQL table

## Requirements
- Ubuntu 14.04 LTS
- MySQL server is in 5.7
- MySQLdb module version 1.3.x
- SQLAlchemy module version 1.2.x

## Challenges

### 0. Get all states
A script that lists all states from the database hbtn_0e_0_usa:
- The script take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
- It is used the module MySQLdb (import MySQLdb)
- Is is connected to a MySQL server running on localhost at port 3306
- Results are sorted in ascending order by states.id
- Results are displayed as they are in the example below
- The code is not executed when imported

**Example**
```bash wrap
guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./0-select_states.py root root hbtn_0e_0_usa
(1, 'California')
(2, 'Arizona')
(3, 'Texas')
(4, 'New York')
(5, 'Nevada')
guillaume@ubuntu:~/0x0F$ 
```

**Answer file:** [0-select_states.py]()

### 1. Filter states

### 2. Filter states by user input

### 3. SQL Injection...

### 4. Cities by states

### 5. All cities by state

### 6. First state model

### 7. All states via SQLAlchemy

### 8. First state

### 9. Contains `a` 

### 10. Get a state

### 11. Add a new state

### 12. Update a state

### 13. Delete states

### 14. Cities in state

## Author
* Gonzalo Gomez Milla  |  :octocat:  [Github](https://github.com/gogomillan)
