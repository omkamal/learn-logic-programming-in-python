from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, parent, grandparent')
for a, b in [('alice', 'bob'), ('alice', 'carol'), ('bob', 'dave'),
             ('carol', 'erin')]:
    +parent(a, b)

grandparent(X, Z) <= parent(X, Y)       # Z never appears in the body
print(grandparent(X, Z))                 # True, not a table
print(bool(grandparent('alice', 'zzz')))
