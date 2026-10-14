from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, parent_a, parent_b')

+parent_a('alice', 'bob')       # typed top to bottom
+parent_a('alice', 'carol')
+parent_a('bob', 'dave')
+parent_a('carol', 'erin')

+parent_b('carol', 'erin')      # the same four cards, typed backwards
+parent_b('bob', 'dave')
+parent_b('alice', 'carol')
+parent_b('alice', 'bob')

print(sorted(parent_a(X, Y).data) == sorted(parent_b(X, Y).data))
