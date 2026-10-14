import sqlite3

db = sqlite3.connect(':memory:')
db.execute('CREATE TABLE employee (name TEXT PRIMARY KEY, '
           'manager_name TEXT, salary INTEGER)')
db.executemany('INSERT INTO employee VALUES (?, ?, ?)',
               [('ann', None, 150), ('bob', 'ann', 100),
                ('cid', 'bob', 80), ('dee', 'bob', 90)])

# everyone above cid, as a recursive common table expression
rows = db.execute("""
    WITH RECURSIVE above(name) AS (
        SELECT manager_name FROM employee WHERE name = 'cid'
        UNION
        SELECT e.manager_name FROM employee e JOIN above a
            ON e.name = a.name
    )
    SELECT name FROM above WHERE name IS NOT NULL ORDER BY name""")
print(rows.fetchall())
