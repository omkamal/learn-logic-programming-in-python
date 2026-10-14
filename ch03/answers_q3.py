from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, P, A, N, mother, father, parent, sibling, '
                       'aunt_or_uncle')

+mother('alice', 'bob')
+mother('alice', 'carol')
+father('frank', 'bob')
+father('frank', 'carol')
+father('bob', 'dave')
+mother('carol', 'erin')

parent(X, Y) <= mother(X, Y)
parent(X, Y) <= father(X, Y)
sibling(X, Y) <= parent(P, X) & parent(P, Y) & (X != Y)

aunt_or_uncle(A, N) <= sibling(A, P) & parent(P, N)

print(sorted(aunt_or_uncle(A, N).data))
