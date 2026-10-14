from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, P, parent, mother, father, sibling')

+mother('alice', 'bob')
+mother('alice', 'carol')
+father('frank', 'bob')
+father('frank', 'carol')

# two clauses for the same head = OR
parent(X, Y) <= mother(X, Y)
parent(X, Y) <= father(X, Y)

print(parent(X, 'bob'))

# a shared parent and an inequality
sibling(X, Y) <= parent(P, X) & parent(P, Y) & (X != Y)
print(sibling('bob', Y))
