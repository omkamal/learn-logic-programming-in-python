from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, P, mother, father, parent, shared')

+mother('alice', 'bob')
+mother('alice', 'carol')
+father('frank', 'bob')
+father('frank', 'carol')

parent(X, Y) <= mother(X, Y)
parent(X, Y) <= father(X, Y)

# before the inequality: every shared parent P with every candidate Y
shared(P, X, Y) <= parent(P, X) & parent(P, Y)
print(sorted(shared(P, 'bob', Y).data))
