-- COUNT(*) counts rows; COUNT(DISTINCT name) counts different names.
CREATE TABLE pupil(name TEXT, class TEXT);
INSERT INTO pupil VALUES
  ('sam', '7a'), ('sam', '7a'), ('amy', '7a'),
  ('zoe', '7b'), ('zoe', '7b');
SELECT class, COUNT(*), COUNT(DISTINCT name)
FROM pupil GROUP BY class ORDER BY class;
