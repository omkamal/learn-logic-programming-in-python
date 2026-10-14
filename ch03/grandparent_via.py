from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, parent, via')

+parent('alice', 'bob')
+parent('alice', 'carol')
+parent('bob', 'dave')
+parent('carol', 'erin')

# the same join, but the head keeps the shared name Y
via(X, Y, Z) <= parent(X, Y) & parent(Y, Z)

print(sorted(via(X, Y, Z).data))
