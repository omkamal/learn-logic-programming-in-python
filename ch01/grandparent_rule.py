# The clerk with the index cards: state what is true, then ask.
from pyDatalog import pyDatalog

pyDatalog.create_terms('parent, grandparent, X, Y, Z')

+parent('alice', 'bob')
+parent('alice', 'carol')
+parent('bob', 'dave')
+parent('carol', 'erin')

grandparent(X, Z) <= parent(X, Y) & parent(Y, Z)

print(sorted(grandparent(X, Z).data))        # every grandparent pair
print(sorted(grandparent('alice', Z).data))  # whose grandparent is alice?
print(sorted(grandparent(X, 'erin').data))   # who is erin's grandparent?
