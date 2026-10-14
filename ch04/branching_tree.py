from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, parent, ancestor')

+parent('alice', 'bob')
+parent('alice', 'carol')
+parent('bob', 'dave')
+parent('carol', 'erin')

ancestor(X, Y) <= parent(X, Y)
ancestor(X, Y) <= ancestor(X, Z) & parent(Z, Y)

for pair in sorted(ancestor(X, Y).data):
    print(pair)
