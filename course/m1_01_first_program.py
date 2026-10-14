from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, parent, grandparent')

# facts
+parent('alice', 'bob')
+parent('alice', 'carol')
+parent('bob', 'dave')
+parent('carol', 'erin')

# a query
print(parent('alice', X))
print(parent(X, 'dave'))
print(parent(X, Y))

# a rule
grandparent(X, Z) <= parent(X, Y) & parent(Y, Z)
print(grandparent('alice', Z))
print(grandparent(X, Y))
