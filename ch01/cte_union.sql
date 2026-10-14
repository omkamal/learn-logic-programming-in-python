-- The flights as a table, then a recursive query that follows them.
CREATE TABLE flight(src TEXT, dst TEXT);
INSERT INTO flight VALUES
  ('CAI','DXB'), ('DXB','LHR'), ('LHR','CAI'), ('LHR','JFK');

WITH RECURSIVE reach(city) AS (
    SELECT dst FROM flight WHERE src = 'CAI'       -- base: one flight
  UNION
    SELECT flight.dst                              -- step: one more flight
    FROM reach JOIN flight ON flight.src = reach.city
)
SELECT city FROM reach ORDER BY city;
