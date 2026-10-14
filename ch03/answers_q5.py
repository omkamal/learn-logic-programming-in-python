from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, parent, grandparent')

+parent('alice', 'bob')
+parent('alice', 'carol')
+parent('bob', 'dave')
+parent('carol', 'erin')

grandparent(X, Z) <= parent(X, Y) & parent(Y, Z)

print(sorted(grandparent(X, Z).data))
-parent('alice', 'bob')
print(sorted(grandparent(X, Z).data))
