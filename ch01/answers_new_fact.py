# Exercise 3 of Chapter 1: one new card, and the same rule.
from pyDatalog import pyDatalog

pyDatalog.create_terms('parent, grandparent, X, Y, Z')

+parent('alice', 'bob')
+parent('alice', 'carol')
+parent('bob', 'dave')
+parent('carol', 'erin')
+parent('erin', 'fay')          # the new card

grandparent(X, Z) <= parent(X, Y) & parent(Y, Z)

print(sorted(grandparent(X, Z).data))
