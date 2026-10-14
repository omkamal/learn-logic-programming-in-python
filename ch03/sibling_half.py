from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, P, mother, father, parent, sibling')

+mother('alice', 'bob')
+mother('alice', 'carol')
+father('frank', 'bob')
+father('gus', 'carol')          # Carol's father is somebody else

parent(X, Y) <= mother(X, Y)
parent(X, Y) <= father(X, Y)
sibling(X, Y) <= parent(P, X) & parent(P, Y) & (X != Y)

print(sorted(sibling('bob', Y).data))
