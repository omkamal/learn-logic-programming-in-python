from pyDatalog import pyDatalog

pyDatalog.create_terms('X, parent')

+parent('alice', 'bob')     # parent with two slots
+parent('alice')            # parent with ONE slot: no error

print(parent('alice', X))   # the two-slot table
print(parent(X))            # the one-slot table
