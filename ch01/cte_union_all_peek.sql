-- UNION ALL on the loop; only peek at the first 12 rows of the stream.
CREATE TABLE flight(src TEXT, dst TEXT);
INSERT INTO flight VALUES
  ('CAI','DXB'), ('DXB','LHR'), ('LHR','CAI'), ('LHR','JFK');

WITH RECURSIVE reach(city, hops) AS (
    SELECT dst, 1 FROM flight WHERE src = 'CAI'
  UNION ALL
    SELECT flight.dst, reach.hops + 1
    FROM reach JOIN flight ON flight.src = reach.city
)
SELECT hops, city FROM reach LIMIT 12;
