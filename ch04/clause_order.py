from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, parent, up, down')

+parent('alice', 'bob')
+parent('bob', 'carol')
+parent('carol', 'dave')

# up: base clause first.  down: the same two clauses, swapped.
up(X, Y) <= parent(X, Y)
up(X, Y) <= up(X, Z) & parent(Z, Y)

down(X, Y) <= down(X, Z) & parent(Z, Y)
down(X, Y) <= parent(X, Y)

print(sorted(up(X, Y).data) == sorted(down(X, Y).data))
print(len(up(X, Y).data), len(down(X, Y).data))
