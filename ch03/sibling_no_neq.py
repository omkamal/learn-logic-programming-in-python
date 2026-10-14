from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, P, mother, father, parent, sibling')

+mother('alice', 'bob')
+mother('alice', 'carol')
+father('frank', 'bob')
+father('frank', 'carol')
+father('bob', 'dave')
+mother('carol', 'erin')

parent(X, Y) <= mother(X, Y)
parent(X, Y) <= father(X, Y)

sibling(X, Y) <= parent(P, X) & parent(P, Y)      # no inequality

print(sorted(sibling('bob', Y).data))
print(len(sibling(X, Y).data), 'sibling pairs')
