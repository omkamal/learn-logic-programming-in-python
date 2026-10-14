# Try-it 1: a ring of 200 towns plus one chord from town 0 to town 100.
import sqlite3

N = 200
edges = [(i, (i + 1) % N) for i in range(N)] + [(0, 100)]
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE flight(src INT, dst INT)")
db.executemany("INSERT INTO flight VALUES (?,?)", edges)
q = """WITH RECURSIVE reach(src, dst) AS (
           SELECT src, dst FROM flight
         UNION
           SELECT reach.src, flight.dst
           FROM reach JOIN flight ON flight.src = reach.dst)
       SELECT count(*) FROM reach"""
print("pairs with the chord:", db.execute(q).fetchone()[0], "of", N * N)
