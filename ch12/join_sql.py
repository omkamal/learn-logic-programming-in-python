import sqlite3

db = sqlite3.connect(':memory:')
db.execute('CREATE TABLE supplier (name TEXT PRIMARY KEY, city TEXT)')
db.execute('CREATE TABLE product (name TEXT PRIMARY KEY, '
           'supplier_name TEXT REFERENCES supplier(name), cents INTEGER)')
db.executemany('INSERT INTO supplier VALUES (?, ?)',
               [('acme', 'cairo'), ('bolt', 'dubai'), ('cedar', 'london')])
db.executemany('INSERT INTO product VALUES (?, ?, ?)',
               [('pen', 'acme', 300), ('book', 'bolt', 1200),
                ('lamp', 'acme', 1999), ('desk', 'bolt', 8900),
                ('mug', None, 450)])

# the same join in plain SQL: one statement, done by the database
rows = db.execute("""SELECT product.name, supplier.city
                     FROM product JOIN supplier
                       ON product.supplier_name = supplier.name
                     ORDER BY product.name""")
print(rows.fetchall())
