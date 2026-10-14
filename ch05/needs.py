from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, needs, needs_all, stuck')
for a, b in [('bread', 'starter'), ('bread', 'flour'), ('bread', 'salt'),
             ('starter', 'flour'), ('starter', 'water'),
             ('starter', 'scraps'), ('scraps', 'bread')]:
    +needs(a, b)

needs_all(X, Y) <= needs(X, Y)
needs_all(X, Y) <= needs_all(X, Z) & needs(Z, Y)     # recursive FIRST

stuck(X) <= needs_all(X, X)         # something that needs itself

print(sorted(needs_all('bread', Y).data))
print(sorted(stuck(X).data))

-needs('starter', 'scraps')         # feed the starter without scraps
print(sorted(stuck(X).data))
