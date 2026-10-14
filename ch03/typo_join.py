from pyDatalog import pyDatalog

pyDatalog.create_terms('W, X, Y, Z, parent, grandparent')

+parent('alice', 'bob')
+parent('alice', 'carol')
+parent('bob', 'dave')
+parent('carol', 'erin')

# a slip: the second condition says W, not Y, so nothing is shared
grandparent(X, Z) <= parent(X, Y) & parent(W, Z)

pairs = sorted(grandparent(X, Z).data)
print(len(pairs), 'pairs, the first two:', pairs[:2])
print(('alice', 'bob') in pairs)
