from pyDatalog import pyDatalog

pyDatalog.create_terms('x, parent')
+parent('alice', 'bob')
+parent('alice', 'carol')

print(parent('alice', x))
