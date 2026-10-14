from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, parent, ancestor')

+parent('alice', 'bob')
+parent('bob', 'carol')
+parent('carol', 'dave')

# the recursive clause only: the base case is missing
ancestor(X, Y) <= ancestor(X, Z) & parent(Z, Y)

print(ancestor('alice', Y))
print(ancestor(X, Y))
print(bool(ancestor('alice', 'dave')))
