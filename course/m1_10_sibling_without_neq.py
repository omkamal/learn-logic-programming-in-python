# The sibling rule WITHOUT the inequality
from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, P, parent, sibling')
+parent('alice', 'bob')
+parent('alice', 'carol')
sibling(X, Y) <= parent(P, X) & parent(P, Y)
print(sorted(sibling('bob', Y).data))
