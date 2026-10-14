from pyDatalog import pyDatalog

pyDatalog.create_terms('X, parent')
+parent('alice', 'bob')
+parent('alice', 'carol')

print(sorted(parent('alice', X).data))
print(parent('alice', X).v())      # looks like "all the values of X"
