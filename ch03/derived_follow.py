from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, parent, grandparent')

+parent('alice', 'bob')
+parent('alice', 'carol')
+parent('bob', 'dave')
+parent('carol', 'erin')

grandparent(X, Z) <= parent(X, Y) & parent(Y, Z)
print(sorted(grandparent(X, Z).data))

-parent('bob', 'dave')            # take one STATED card out
print(sorted(grandparent(X, Z).data))
+parent('bob', 'dave')            # put it back
print(sorted(grandparent(X, Z).data))

-grandparent('alice', 'dave')     # try to erase a DERIVED card
print(sorted(grandparent(X, Z).data))
