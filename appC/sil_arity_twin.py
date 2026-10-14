from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, parent')
+parent('alice', 'bob')
+parent('alice')                   # one slot: a different table, parent/1

print(sorted(parent('alice', Y).data))
print(sorted(parent(X).data))
