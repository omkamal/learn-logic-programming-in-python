import sqlite3

db = sqlite3.connect(':memory:')        # a database that lives in memory
db.execute("""CREATE TABLE employee (
    name TEXT PRIMARY KEY,
    manager_name TEXT REFERENCES employee(name),
    salary INTEGER)""")
db.executemany('INSERT INTO employee VALUES (?, ?, ?)',
               [('ann', None, 150), ('bob', 'ann', 100),
                ('cid', 'bob', 80), ('dee', 'bob', 90)])

def ask(sql):
    print(sql)
    for row in db.execute(sql):
        print('   ', row)

ask('SELECT * FROM employee')
ask('SELECT name FROM employee WHERE salary > 85')
ask('SELECT name FROM employee WHERE manager_name IS NULL')
