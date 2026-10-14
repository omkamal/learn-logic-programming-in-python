from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, mother, father, parent, grandparent')

+mother('alice', 'bob')
+mother('alice', 'carol')
+father('frank', 'bob')
+father('frank', 'carol')
+father('bob', 'dave')
+mother('carol', 'erin')

parent(X, Y) <= mother(X, Y)
parent(X, Y) <= father(X, Y)

print(parent(X, 'bob'))
print(len(parent(X, Y).data), 'parent pairs, none of them stated')

grandparent(X, Z) <= parent(X, Y) & parent(Y, Z)
print(sorted(grandparent(X, Z).data))
