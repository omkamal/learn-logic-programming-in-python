from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, parent, grandparent, swapped')
for a, b in [('alice', 'bob'), ('alice', 'carol'),
             ('bob', 'dave'), ('carol', 'erin')]:
    +parent(a, b)

grandparent(X, Z) <= parent(X, Y) & parent(Y, Z)
swapped(X, Z) <= parent(Y, Z) & parent(X, Y)    # same two literals

print(sorted(grandparent(X, Z).data))
print(sorted(swapped(X, Z).data))
