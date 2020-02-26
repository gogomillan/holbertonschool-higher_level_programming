-- Script that lists all cities contained in the database hbtn_0d_usa plus the state name.
-- Select left join
SELECT c.id, c.name, s.name
FROM   cities c LEFT JOIN states s
  ON   s.id = c.state_id
ORDER BY c.id;
