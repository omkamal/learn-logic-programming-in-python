# timeout: 6
import sqlite3

db = sqlite3.connect(':memory:')
db.execute('CREATE TABLE flight(src TEXT, dst TEXT)')
db.executemany('INSERT INTO flight VALUES (?, ?)',
               [('CAI', 'DXB'), ('DXB', 'LHR'), ('LHR', 'CAI'),
                ('LHR', 'JFK')])
union = """WITH RECURSIVE reach(city) AS (
    SELECT dst FROM flight WHERE src = 'CAI'
  UNION %s
    SELECT flight.dst FROM reach JOIN flight ON flight.src = reach.city
) SELECT count(*) FROM reach"""
print('UNION:    ', db.execute(union % '').fetchone())
print('UNION ALL: asking')
print(db.execute(union % 'ALL').fetchone())
