-- timeout: 5
-- The same query with UNION ALL instead of UNION, asking for a count.
CREATE TABLE flight(src TEXT, dst TEXT);
INSERT INTO flight VALUES
  ('CAI','DXB'), ('DXB','LHR'), ('LHR','CAI'), ('LHR','JFK');

WITH RECURSIVE reach(city) AS (
    SELECT dst FROM flight WHERE src = 'CAI'
  UNION ALL
    SELECT flight.dst
    FROM reach JOIN flight ON flight.src = reach.city
)
SELECT count(*) FROM reach;
