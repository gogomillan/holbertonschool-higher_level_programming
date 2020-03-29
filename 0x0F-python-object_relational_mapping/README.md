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
Script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. But, in a safe way to avoid MySQL injections!
- The script takes 4 arguments: mysql username, mysql password, database name and state name searched (safe from SQL injection)
- The module MySQLdb (import MySQLdb) is used
- It is connected to a MySQL server running on localhost at port 3306
- It is used format to create the SQL query with the user input
- Results are sorted in ascending order by states.id
- Results are displayed as they are in the example below
- The code is not executed when imported

**Example 1 of 2**
```bash wrap
guillaume@ubuntu:~/0x0F$ ./2-my_filter_states.py root root hbtn_0e_0_usa "Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '"
(2, 'Arizona')
guillaume@ubuntu:~/0x0F$ ./0-select_states.py root root hbtn_0e_0_usa
guillaume@ubuntu:~/0x0F$ 
```
What? Empty? Yes, its an SQL injection to delete all records of a table  

**Example 2 of 2**
```
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
guillaume@ubuntu:~/0x0F$ ./3-my_safe_filter_states.py root root hbtn_0e_0_usa 'Arizona'
(2, 'Arizona')
guillaume@ubuntu:~/0x0F$ 
```

**Answer file:** [3-my_safe_filter_states.py](https://github.com/gogomillan/holbertonschool-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/3-my_safe_filter_states.py)

### 4. Cities by states
Script that lists all cities from the database hbtn_0e_4_usa
- The script takes 3 arguments: mysql username, mysql password and database name
- The module MySQLdb (import MySQLdb) is used
- It is connected to a MySQL server running on localhost at port 3306
- It is used only once execute()
- Results are sorted in ascending order by cities.id
- Results are displayed as they are in the example below
- The code is not executed when imported

**Example**
```
guillaume@ubuntu:~/0x0F$ cat 4-cities_by_state.sql
-- Create states table in hbtn_0e_4_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_4_usa;
USE hbtn_0e_4_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

CREATE TABLE IF NOT EXISTS cities ( 
    id INT NOT NULL AUTO_INCREMENT, 
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(state_id) REFERENCES states(id)
);
INSERT INTO cities (state_id, name) VALUES (1, "San Francisco"), (1, "San Jose"), (1, "Los Angeles"), (1, "Fremont"), (1, "Livermore");
INSERT INTO cities (state_id, name) VALUES (2, "Page"), (2, "Phoenix");
INSERT INTO cities (state_id, name) VALUES (3, "Dallas"), (3, "Houston"), (3, "Austin");
INSERT INTO cities (state_id, name) VALUES (4, "New York");
INSERT INTO cities (state_id, name) VALUES (5, "Las Vegas"), (5, "Reno"), (5, "Henderson"), (5, "Carson City");

guillaume@ubuntu:~/0x0F$ cat 4-cities_by_state.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./4-cities_by_state.py root root hbtn_0e_4_usa
(1, 'San Francisco', 'California')
(2, 'San Jose', 'California')
(3, 'Los Angeles', 'California')
(4, 'Fremont', 'California')
(5, 'Livermore', 'California')
(6, 'Page', 'Arizona')
(7, 'Phoenix', 'Arizona')
(8, 'Dallas', 'Texas')
(9, 'Houston', 'Texas')
(10, 'Austin', 'Texas')
(11, 'New York', 'New York')
(12, 'Las Vegas', 'Nevada')
(13, 'Reno', 'Nevada')
(14, 'Henderson', 'Nevada')
(15, 'Carson City', 'Nevada')
guillaume@ubuntu:~/0x0F$
```

**Answer file:** [4-cities_by_state.py](https://github.com/gogomillan/holbertonschool-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/4-cities_by_state.py)

### 5. All cities by state
Script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa
- The script takes 4 arguments: mysql username, mysql password, database name and state name searched (safe from SQL injection)
- The module MySQLdb (import MySQLdb) is used
- It is connected to a MySQL server running on localhost at port 3306
- Results are sorted in ascending order by cities.id
- Results are displayed as they are in the example below
- The code is not executed when imported

**Example**
```
guillaume@ubuntu:~/0x0F$ cat 4-cities_by_state.sql
-- Create states table in hbtn_0e_4_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_4_usa;
USE hbtn_0e_4_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

CREATE TABLE IF NOT EXISTS cities ( 
    id INT NOT NULL AUTO_INCREMENT, 
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(state_id) REFERENCES states(id)
);
INSERT INTO cities (state_id, name) VALUES (1, "San Francisco"), (1, "San Jose"), (1, "Los Angeles"), (1, "Fremont"), (1, "Livermore");
INSERT INTO cities (state_id, name) VALUES (2, "Page"), (2, "Phoenix");
INSERT INTO cities (state_id, name) VALUES (3, "Dallas"), (3, "Houston"), (3, "Austin");
INSERT INTO cities (state_id, name) VALUES (4, "New York");
INSERT INTO cities (state_id, name) VALUES (5, "Las Vegas"), (5, "Reno"), (5, "Henderson"), (5, "Carson City");

guillaume@ubuntu:~/0x0F$ cat 4-cities_by_state.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./5-filter_cities.py root root hbtn_0e_4_usa Texas
Dallas, Houston, Austin
guillaume@ubuntu:~/0x0F$ 
```

**Answer file:** [5-filter_cities.py](https://github.com/gogomillan/holbertonschool-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/5-filter_cities.py)

### 6. First state model
Python module that contains the class definition of a State and an instance of Base = declarative_base():
- State class:
  - inherits from Base Tips
  - links to the MySQL table states
  - class attribute id that represents a column of an auto-generated, unique integer, cant be null and is a primary key
  - class attribute name that represents a column of a string with maximum 128 characters and cant be null
- The module SQLAlchemy is used
- The MySQL server runs on localhost at port 3306

**Example**
```
guillaume@ubuntu:~/0x0F$ cat 6-model_state.sql
-- Create database hbtn_0e_6_usa
CREATE DATABASE IF NOT EXISTS hbtn_0e_6_usa;
USE hbtn_0e_6_usa;
SHOW CREATE TABLE states;

guillaume@ubuntu:~/0x0F$ cat 6-model_state.sql | mysql -uroot -p
Enter password: 
ERROR 1146 (42S02) at line 4: Table 'hbtn_0e_6_usa.states' doesn't exist
guillaume@ubuntu:~/0x0F$ cat 6-model_state.py
#!/usr/bin/python3
"""Start link class to table in database 
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

guillaume@ubuntu:~/0x0F$ ./6-model_state.py root root hbtn_0e_6_usa
guillaume@ubuntu:~/0x0F$ cat 6-model_state.sql | mysql -uroot -p
Enter password: 
Table   Create Table
states  CREATE TABLE `states` (\n  `id` int(11) NOT NULL AUTO_INCREMENT,\n  `name` varchar(128) NOT NULL,\n  PRIMARY KEY (`id`)\n) ENGINE=InnoDB DEFAULT CHARSET=latin1
guillaume@ubuntu:~/0x0F$ 
```

**Answer file:** [model_state.py](https://github.com/gogomillan/holbertonschool-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/model_state.py)

### 7. All states via SQLAlchemy
Python module that lists all State objects from the database hbtn_0e_6_usa
- The script takes 3 arguments: mysql username, mysql password and database name
- The module SQLAlchemy is used
- It is imported State and Base from model_state
- It is connected to a MySQL server running on localhost at port 3306
- Results are sorted in ascending order by states.id
- The results are displayed as they are in the example below
- The code is not executed when imported

**Example**
```
guillaume@ubuntu:~/0x0F$ cat 7-model_state_fetch_all.sql
-- Insert states
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:~/0x0F$ cat 7-model_state_fetch_all.sql | mysql -uroot -p hbtn_0e_6_usa
Enter password: 
guillaume@ubuntu:~/0x0F$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa
1: California
2: Arizona
3: Texas
4: New York
5: Nevada
guillaume@ubuntu:~/0x0F$ 
```

**Answer file:** [7-model_state_fetch_all.py](https://github.com/gogomillan/holbertonschool-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/7-model_state_fetch_all.py)

### 8. First state
Python module that prints the first State object from the database hbtn_0e_6_usa:
- The script takes 3 arguments: mysql username, mysql password and database name
- The module SQLAlchemy is used
- It is imported State and Base from model_state
- It is connected to a MySQL server running on localhost at port 3306
- Results are sorted in ascending order by states.id
- The results are displayed as they are in the example below
- If the table states is empty, print Nothing followed by a new line
- The code is not executed when imported

**Example**
```
guillaume@ubuntu:~/0x0F$ ./8-model_state_fetch_first.py root root hbtn_0e_6_usa
1: California
guillaume@ubuntu:~/0x0F$ 
```

**Answer file:** [8-model_state_fetch_first.py](https://github.com/gogomillan/holbertonschool-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/8-model_state_fetch_first.py)

### 9. Contains 'a' 
Python module that lists all State objects that contain the letter a from the database hbtn_0e_6_usa:
- The script takes 3 arguments: mysql username, mysql password and database name
- The module SQLAlchemy is used
- It is imported State and Base from model_state
- It is connected to a MySQL server running on localhost at port 3306
- Results are sorted in ascending order by states.id
- The results are displayed as they are in the example below
- The code is not executed when imported

**Example**
```
guillaume@ubuntu:~/0x0F$ ./9-model_state_filter_a.py root root hbtn_0e_6_usa
1: California
2: Arizona
3: Texas
5: Nevada
guillaume@ubuntu:~/0x0F$ 
```

**Answer file:** [9-model_state_filter_a.py](https://github.com/gogomillan/holbertonschool-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/9-model_state_filter_a.py)

### 10. Get a state

### 11. Add a new state

### 12. Update a state

### 13. Delete states

### 14. Cities in state

## Author
* Gonzalo Gomez Milla  |  :octocat:  [Github](https://github.com/gogomillan)
