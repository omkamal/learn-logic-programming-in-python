from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, parent, related')

+parent('alice', 'bob')
+parent('alice', 'carol')
+parent('bob', 'dave')
+parent('carol', 'erin')

related(X, Y) <= parent(X, Y)
related(X, Y) <= parent(Y, X)

print(len(related(X, Y).data), 'rows')
print(sorted(related('bob', Y).data))
