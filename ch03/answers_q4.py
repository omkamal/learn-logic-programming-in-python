from pyDatalog import pyDatalog

pyDatalog.create_terms('W, X, Y, Z, parent, pair')

+parent('alice', 'bob')
+parent('bob', 'carol')

pair(X, Z) <= parent(X, Y) & parent(W, Z)

print(sorted(pair(X, Z).data))
