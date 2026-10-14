from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, mother, father, guardian, parent')

+mother('alice', 'bob')
+father('bob', 'dave')

parent(X, Y) <= mother(X, Y)
parent(X, Y) <= father(X, Y)
print(sorted(parent(X, 'dave').data))

+guardian('gus', 'dave')              # a new kind of card ...
parent(X, Y) <= guardian(X, Y)        # ... and a third clause
print(sorted(parent(X, 'dave').data))
print(sorted(parent('alice', Y).data))
