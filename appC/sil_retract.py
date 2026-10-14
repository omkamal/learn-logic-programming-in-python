from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, parent, grandparent')
for a, b in [('alice', 'bob'), ('bob', 'dave')]:
    +parent(a, b)
grandparent(X, Z) <= parent(X, Y) & parent(Y, Z)
print(sorted(grandparent(X, Z).data))

-grandparent('alice', 'dave')            # a derived card cannot be erased
print(sorted(grandparent(X, Z).data))
-parent('alice', 'zed')                  # a card that was never there
print(sorted(parent(X, Z).data))
