from pyDatalog import pyDatalog

pyDatalog.create_terms('X, parent')
+parent('alice', 'bob')
+parent('alice', 'carol')

q = parent('alice', X)
print(len(q.data), 'answer rows in .data')
row = q.v()
print(type(row).__name__, len(row), '<- what .v() returns: one row')
