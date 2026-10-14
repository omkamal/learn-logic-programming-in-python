.headers on
.mode column
CREATE TABLE sale (id INTEGER, region TEXT, amount INTEGER);
INSERT INTO sale VALUES (1, 'north', 50), (2, 'north', 70),
                        (3, 'south', 30), (4, 'south', 90),
                        (5, 'west', 60), (6, 'north', 50);

SELECT region, SUM(amount) AS per_sale, SUM(DISTINCT amount) AS per_amount
FROM sale
GROUP BY region
ORDER BY region;
