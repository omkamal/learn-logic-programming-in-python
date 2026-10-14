from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, parent')

+parent('alice', 'bob')
+parent('alice', 'carol')
+parent('bob', 'dave')
+parent('carol', 'erin')

print(parent('alice', X))
