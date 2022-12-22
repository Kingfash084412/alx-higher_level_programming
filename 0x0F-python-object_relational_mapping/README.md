# 0x0F. Python - Object-relational mapping

## Learning Objectives

- What ORM means
- How to connect to a MySQL database from a Python script
- How to map a Python Class to a MySQL table
- How to prevent SQL Injection

## Requirements

- All files are created and executed on Ubuntu 20.04 LTS using MySQL 8.0 and Python3 (version 3.4.3)
- All Python code use the PEP 8 style (version 1.7.\*)

## Tasks

<details>
<summary>View Contents</summary>

### [0. Get all states](./0-select_states.py)

- Write a script that lists all states from the database hbtn_0e_0_usa:
  - Results must be sorted in ascending order by states.id
  - Results must be displayed as they are in the example below

```
guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql
```

```sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");
```

```
guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql | mysql -uroot -p
Enter password:
guillaume@ubuntu:~/0x0F$ ./0-select_states.py root root hbtn_0e_0_usa
(1, 'California')
(2, 'Arizona')
(3, 'Texas')
(4, 'New York')
(5, 'Nevada')
```

### [1. Filter states](./1-filter_states.py)

- Write a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa:
  - Results must be sorted in ascending order by states.id
  - Results must be displayed as they are in the example below

```
guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql
```

```sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");
```

```
guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql | mysql -uroot -p
Enter password:
guillaume@ubuntu:~/0x0F$ ./1-filter_states.py root root hbtn_0e_0_usa
(4, 'New York')
(5, 'Nevada')
```

### [2. Filter states by user input](./2-my_filter_states.py)

- Write a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
  - Results must be sorted in ascending order by states.id

```
guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql
```

```sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");
```

```
guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql | mysql -uroot -p
Enter password:
guillaume@ubuntu:~/0x0F$ ./2-my_filter_states.py root root hbtn_0e_0_usa 'Arizona'
(2, 'Arizona')
```

### [3. SQL Injection...](./3-my_safe_filter_states.py)

- Wait, do you remember the previous task? Did you test "Arizona'; TRUNCATE TABLE states ; SELECT \* FROM states WHERE name = '" as an input?
  - Results must be sorted in ascending order by states.id

```
guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql
```

```sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");
```

```
guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql | mysql -uroot -p
Enter password:
guillaume@ubuntu:~/0x0F$ ./3-my_safe_filter_states.py root root hbtn_0e_0_usa 'Arizona'
(2, 'Arizona')
```

### [4. Cities by states](./4-cities_by_state.py)

- Write a script that lists all cities from the database hbtn_0e_4_usa
  - Results must be sorted in ascending order by cities.id
  - You can use only execute() once

```
guillaume@ubuntu:~/0x0F$ cat 4-cities_by_state.sql
```

```sql
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
```

```
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
```

### [5. All cities by state](./5-filter_cities.py)

- Write a script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa
  - Results must be sorted in ascending order by cities.id
  - You can use only execute() once

```
guillaume@ubuntu:~/0x0F$ cat 4-cities_by_state.sql
```

```sql
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
```

```
guillaume@ubuntu:~/0x0F$ cat 4-cities_by_state.sql | mysql -uroot -p
Enter password:
guillaume@ubuntu:~/0x0F$ ./5-filter_cities.py root root hbtn_0e_4_usa Texas
Dallas, Houston, Austin
```

### [6. First state model](./model_state.py)

- Write a python file that contains the class definition of a State and an instance Base = declarative_base():
- State class:
  - Inherits from Base Tips
  - links to the MySQL table states
  - class attribute id that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
  - class attribute name that represents a column of a string with maximum 128 characters and can’t be null

```
guillaume@ubuntu:~/0x0F$ cat 6-model_state.sql | mysql -uroot -p
Enter password:
ERROR 1146 (42S02) at line 4: Table 'hbtn_0e_6_usa.states' doesn't exist
guillaume@ubuntu:~/0x0F$ cat 6-model_state.py
```

```py
#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
```

```
guillaume@ubuntu:~/0x0F$ ./6-model_state.py root root hbtn_0e_6_usa
guillaume@ubuntu:~/0x0F$ cat 6-model_state.sql | mysql -uroot -p
Enter password:
Table   Create Table
states  CREATE TABLE `states` (\n  `id` int(11) NOT NULL AUTO_INCREMENT,\n  `name` varchar(128) NOT NULL,\n  PRIMARY KEY (`id`)\n) ENGINE=InnoDB DEFAULT CHARSET=latin1
```

### [7. All states via SQLAlchemy](./7-model_state_fetch_all.py)

- Write a script that lists all State objects from the database hbtn_0e_6_usa
  - Results must be sorted in ascending order by states.id

```
guillaume@ubuntu:~/0x0F$ cat 7-model_state_fetch_all.sql
```

```sql
-- Insert states
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");
```

```
guillaume@ubuntu:~/0x0F$ cat 7-model_state_fetch_all.sql | mysql -uroot -p hbtn_0e_6_usa
Enter password:
guillaume@ubuntu:~/0x0F$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa
1: California
2: Arizona
3: Texas
4: New York
5: Nevada
```

### [8. First state](./8-model_state_fetch_first.py)

- Write a script that prints the first State object from the database hbtn_0e_6_usa
  - If the table states is empty, print Nothing followed by a new line
  - You are not allowed to fetch all states from the database before displaying the result

```
guillaume@ubuntu:~/0x0F$ ./8-model_state_fetch_first.py root root hbtn_0e_6_usa
1: California
```

### [9. Contains `a`](./9-model_state_filter_a.py)

- Write a script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa
  - Results must be sorted in ascending order by states.id

```
guillaume@ubuntu:~/0x0F$ ./9-model_state_filter_a.py root root hbtn_0e_6_usa
1: California
2: Arizona
3: Texas
5: Nevada
```

### [10. Get a state](./10-model_state_my_get.py)

- Write a script that prints the State object with the name passed as argument from the database hbtn_0e_6_usa
  - You can assume you have one record with the state name to search
  - Results must display the states.id
  - If no state has the name you searched for, display Not found

```
guillaume@ubuntu:~/0x0F$ ./10-model_state_my_get.py root root hbtn_0e_6_usa Texas
3
guillaume@ubuntu:~/0x0F$ ./10-model_state_my_get.py root root hbtn_0e_6_usa Illinois
Not found
```

### [11. Add a new state](./11-model_state_insert.py)

- Write a script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
  - Print the new states.id after creation

```
guillaume@ubuntu:~/0x0F$ ./11-model_state_insert.py root root hbtn_0e_6_usa
6
guillaume@ubuntu:~/0x0F$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa
1: California
2: Arizona
3: Texas
4: New York
5: Nevada
6: Louisiana
```

### [12. Update a state](./12-model_state_update_id_2.py)

- Write a script that changes the name of a State object from the database hbtn_0e_6_usa
  - Change the name of the State where id = 2 to New Mexico

```
guillaume@ubuntu:~/0x0F$ ./12-model_state_update_id_2.py root root hbtn_0e_6_usa
guillaume@ubuntu:~/0x0F$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa
1: California
2: New Mexico
3: Texas
4: New York
5: Nevada
6: Louisiana
```

### [13. Delete states](./13-model_state_delete_a.py)

- Write a script that deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa

```
guillaume@ubuntu:~/0x0F$ ./13-model_state_delete_a.py root root hbtn_0e_6_usa
guillaume@ubuntu:~/0x0F$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa
2: New Mexico
4: New York
```

### [14. Cities in state](./model_city.py)

- Write a Python file similar to model_state.py named model_city.py that contains the class definition of a City.
- City class:

  - inherits from Base (imported from model_state)
  - links to the MySQL table cities
  - class attribute id that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
  - class attribute name that represents a column of a string of 128 characters and can’t be null
  - class attribute state_id that represents a column of an integer, can’t be null and is a foreign key to states.id

- Results must be sorted in ascending order by cities.id
- Results must be display as they are in the example below (<state name>: (<city id>) <city name>)

```
guillaume@ubuntu:~/0x0F$ cat 14-model_city_fetch_by_state.sql
```

```sql
-- Create database hbtn_0e_14_usa, tables states and cities + some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_14_usa;
USE hbtn_0e_14_usa;

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
```

```
guillaume@ubuntu:~/0x0F$ cat 14-model_city_fetch_by_state.sql | mysql -uroot -p
Enter password:
guillaume@ubuntu:~/0x0F$ ./14-model_city_fetch_by_state.py root root hbtn_0e_14_usa
California: (1) San Francisco
California: (2) San Jose
California: (3) Los Angeles
California: (4) Fremont
California: (5) Livermore
Arizona: (6) Page
Arizona: (7) Phoenix
Texas: (8) Dallas
Texas: (9) Houston
Texas: (10) Austin
New York: (11) New York
Nevada: (12) Las Vegas
Nevada: (13) Reno
Nevada: (14) Henderson
Nevada: (15) Carson City
```

### [15. City relationship](./relationship_city.py)

- Improve the files model_city.py and model_state.py, and save them as relationship_city.py and relationship_state.py:

  - City class:
    - No change
  - State class:
    - In addition to previous requirements, the class attribute cities must represent a relationship with the class City. If the State object is deleted, all linked City objects must be automatically deleted. Also, the reference from a City object to his State should be named state

- Write a script that creates the State “California” with the City “San Francisco” from the database hbtn_0e_100_usa: (100-relationship_states_cities.py)

  - You must use the cities relationship for all State objects

```
guillaume@ubuntu:~/0x0F$ cat 100-relationship_states_cities.sql
```

```sql
-- Create the database hbtn_0e_100_usa
CREATE DATABASE IF NOT EXISTS hbtn_0e_100_usa;
USE hbtn_0e_100_usa;

SELECT * FROM states;
SELECT * FROM cities;
```

```
guillaume@ubuntu:~/0x0F$ cat 100-relationship_states_cities.sql | mysql -uroot -p
Enter password:
ERROR 1146 (42S02) at line 5: Table 'hbtn_0e_100_usa.states' doesn't exist
guillaume@ubuntu:~/0x0F$ ./100-relationship_states_cities.py root root hbtn_0e_100_usa
guillaume@ubuntu:~/0x0F$ cat 100-relationship_states_cities.sql | mysql -uroot -p
Enter password:
id  name
1   California
id  name    state_id
1   San Francisco   1
```

### [16. List relationship](./101-relationship_states_cities_list.py)

- Write a script that lists all State objects, and corresponding City objects, contained in the database hbtn_0e_101_usa
  - You must use the cities relationship for all State objects
  - Results must be sorted in ascending order by states.id and cities.id

```
guillaume@ubuntu:~/0x0F$ cat 101-relationship_states_cities_list.sql
```

```sql
-- Create states table in hbtn_0e_101_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_101_usa;
USE hbtn_0e_101_usa;
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
```

```
guillaume@ubuntu:~/0x0F$ cat 101-relationship_states_cities_list.sql | mysql -uroot -p
guillaume@ubuntu:~/0x0F$ ./101-relationship_states_cities_list.py root root hbtn_0e_101_usa
1: California
    1: San Francisco
    2: San Jose
    3: Los Angeles
    4: Fremont
    5: Livermore
2: Arizona
    6: Page
    7: Phoenix
3: Texas
    8: Dallas
    9: Houston
    10: Austin
4: New York
    11: New York
5: Nevada
    12: Las Vegas
    13: Reno
    14: Henderson
    15: Carson City
```

### [17. From city](./102-relationship_cities_states_list.py)

- Write a script that lists all City objects from the database hbtn_0e_101_usa
  - You must use only one query to the database
  - You must use the state relationship to access to the State object linked to the City object
  - Results must be sorted in ascending order by cities.id

```
guillaume@ubuntu:~/0x0F$ ./102-relationship_cities_states_list.py root root hbtn_0e_101_usa
1: San Francisco -> California
2: San Jose -> California
3: Los Angeles -> California
4: Fremont -> California
5: Livermore -> California
6: Page -> Arizona
7: Phoenix -> Arizona
8: Dallas -> Texas
9: Houston -> Texas
10: Austin -> Texas
11: New York -> New York
12: Las Vegas -> Nevada
13: Reno -> Nevada
14: Henderson -> Nevada
15: Carson City -> Nevada
```

</details>
