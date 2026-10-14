from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, W, parent, grandparent, greatgp')

+parent('alice', 'bob')
+parent('bob', 'carol')
+parent('carol', 'dave')

grandparent(X, Z) <= parent(X, Y) & parent(Y, Z)
greatgp(X, W) <= parent(X, Y) & parent(Y, Z) & parent(Z, W)

print(grandparent(X, Y))
print(greatgp(X, Y))
