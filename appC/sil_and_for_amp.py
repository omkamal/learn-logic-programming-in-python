from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, parent, good, bad')
for a, b in [('alice', 'bob'), ('alice', 'carol'), ('bob', 'dave'),
             ('carol', 'erin')]:
    +parent(a, b)

good(X, Z) <= parent(X, Y) & parent(Y, Z)
bad(X, Z) <= parent(X, Y) and parent(Y, Z)   # Python 'and', not '&'

print(sorted(good(X, Z).data))
print(bad(X, Z))                             # the second condition is gone
print(bool(bad('alice', 'zzz')))
