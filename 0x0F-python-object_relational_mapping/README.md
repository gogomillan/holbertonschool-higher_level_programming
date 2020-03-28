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
- The script takes 3 arguments: mysql username, mysql password and database name
- The module MySQLdb (import MySQLdb) is used
- It is connected to a MySQL server running on localhost at port 3306
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

**Answer file:** [0-select_states.py](https://github.com/gogomillan/holbertonschool-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/0-select_states.py)

### 1. Filter states
Script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa:
- The script takes 3 arguments: mysql username, mysql password and database name
- The module MySQLdb (import MySQLdb) is used
- It is connected to a MySQL server running on localhost at port 3306
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
guillaume@ubuntu:~/0x0F$ ./1-filter_states.py root root hbtn_0e_0_usa
(4, 'New York')
(5, 'Nevada')
guillaume@ubuntu:~/0x0F$
```

**Answer file:** [1-filter_states.py](https://github.com/gogomillan/holbertonschool-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/1-filter_states.py)

### 2. Filter states by user input
Script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
- The script takes 4 arguments: mysql username, mysql password, database name and state name searched
- The module MySQLdb (import MySQLdb) is used
- It is connected to a MySQL server running on localhost at port 3306
- It is used format to create the SQL query with the user input
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
guillaume@ubuntu:~/0x0F$ ./2-my_filter_states.py root root hbtn_0e_0_usa 'Arizona'
(2, 'Arizona')
guillaume@ubuntu:~/0x0F$ 
```

**Answer file:** [2-my_filter_states.py](https://github.com/gogomillan/holbertonschool-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/2-my_filter_states.py)

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
