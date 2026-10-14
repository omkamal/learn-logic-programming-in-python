from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, parent, descendant')

+parent('alice', 'bob')
+parent('bob', 'carol')
+parent('carol', 'dave')

# descendant(X, Y): X is a descendant of Y
descendant(X, Y) <= parent(Y, X)
descendant(X, Y) <= descendant(X, Z) & parent(Y, Z)

print(sorted(descendant('dave', Y).data))
print(sorted(descendant(X, 'bob').data))
