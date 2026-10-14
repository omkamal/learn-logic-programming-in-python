-- timeout: 5
-- UNION again, but each row now also carries a hop counter.
CREATE TABLE flight(src TEXT, dst TEXT);
INSERT INTO flight VALUES
  ('CAI','DXB'), ('DXB','LHR'), ('LHR','CAI'), ('LHR','JFK');

WITH RECURSIVE reach(city, hops) AS (
    SELECT dst, 1 FROM flight WHERE src = 'CAI'
  UNION
    SELECT flight.dst, reach.hops + 1
    FROM reach JOIN flight ON flight.src = reach.city
)
SELECT count(*) FROM reach;
