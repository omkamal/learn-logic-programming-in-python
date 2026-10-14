# The same grandparent question in SQL (sqlite3 is in the standard library)
import sqlite3

db = sqlite3.connect(':memory:')
db.execute('CREATE TABLE parent (parent TEXT, child TEXT)')
db.executemany('INSERT INTO parent VALUES (?, ?)',
               [('alice', 'bob'), ('alice', 'carol'),
                ('bob', 'dave'), ('carol', 'erin')])
query = """
SELECT p1.parent AS grandparent, p2.child AS grandchild
FROM parent AS p1
JOIN parent AS p2 ON p1.child = p2.parent
ORDER BY grandparent, grandchild
"""
print(db.execute(query).fetchall())
