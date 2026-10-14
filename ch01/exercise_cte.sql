-- Exercise 3: who is above cid in the company?
CREATE TABLE employee(name TEXT, manager TEXT);
INSERT INTO employee VALUES
  ('ann', NULL), ('bob', 'ann'), ('cid', 'bob'), ('dee', 'bob');

WITH RECURSIVE above(boss) AS (
    SELECT manager FROM employee WHERE name = 'cid'
  UNION
    SELECT employee.manager
    FROM above JOIN employee ON employee.name = above.boss
    WHERE employee.manager IS NOT NULL
)
SELECT boss FROM above ORDER BY boss;
