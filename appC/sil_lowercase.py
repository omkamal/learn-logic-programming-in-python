from pyDatalog import pyDatalog

pyDatalog.create_terms('X, x, parent')       # x is a constant, not a blank
+parent('alice', 'bob')
+parent('alice', 'carol')

print(sorted(parent('alice', X).data))
print(sorted(parent('alice', x).data))
