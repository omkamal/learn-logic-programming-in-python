# The rule comes BEFORE the facts, and the facts are in reverse order
from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, parent, grandparent')
grandparent(X, Z) <= parent(X, Y) & parent(Y, Z)
+parent('carol', 'erin')
+parent('bob', 'dave')
+parent('alice', 'carol')
+parent('alice', 'bob')
print(sorted(grandparent(X, Z).data))
