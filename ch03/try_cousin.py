from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, P, Q, mother, father, parent, sibling, '
                       'cousin')

+mother('alice', 'bob')
+mother('alice', 'carol')
+father('frank', 'bob')
+father('frank', 'carol')
+father('bob', 'dave')
+mother('carol', 'erin')

parent(X, Y) <= mother(X, Y)
parent(X, Y) <= father(X, Y)
sibling(X, Y) <= parent(P, X) & parent(P, Y) & (X != Y)

cousin(X, Y) <= parent(P, X) & parent(Q, Y) & sibling(P, Q)

print(sorted(cousin(X, Y).data))
