from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, parent, ancestor')

+parent('alice', 'bob')
+parent('bob', 'carol')
+parent('carol', 'dave')

ancestor(X, Y) <= parent(X, Y)
ancestor(X, Y) <= ancestor(X, Z) & parent(Z, Y)

print(ancestor('alice', Y))
print(ancestor(X, 'dave'))
