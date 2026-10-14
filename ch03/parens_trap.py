# timeout: 10
from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, P, parent, sibling')

+parent('alice', 'bob')
+parent('alice', 'carol')

print('about to state the rule')
sibling(X, Y) <= parent(P, X) & parent(P, Y) & X != Y   # no parentheses
print('rule stated; now asking')
print(sorted(sibling('bob', Y).data))
