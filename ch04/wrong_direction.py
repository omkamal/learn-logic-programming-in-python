from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, parent, ancestor')

+parent('alice', 'bob')
+parent('bob', 'carol')
+parent('carol', 'dave')

ancestor(X, Y) <= parent(X, Y)
ancestor(X, Y) <= ancestor(X, Z) & parent(Y, Z)   # parent written backwards

print(ancestor('alice', Y))
print(bool(ancestor('alice', 'alice')))
