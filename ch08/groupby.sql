.headers on
.mode column
CREATE TABLE emp (name TEXT, dept TEXT, salary INTEGER);
INSERT INTO emp VALUES ('ann', 'eng', 120), ('bob', 'eng', 100),
                       ('cid', 'ops', 80), ('dee', 'ops', 90),
                       ('eli', 'hr', 70);

SELECT dept, SUM(salary) AS total, COUNT(*) AS headcount,
       MAX(salary) AS top
FROM emp
GROUP BY dept
ORDER BY dept;

-- bob gets a raise to 120, exactly like ann
UPDATE emp SET salary = 120 WHERE name = 'bob';

SELECT dept, SUM(salary) AS total, SUM(DISTINCT salary) AS distinct_total
FROM emp
GROUP BY dept
ORDER BY dept;
