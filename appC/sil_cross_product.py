from pyDatalog import pyDatalog

pyDatalog.create_terms('W, X, Y, Z, parent, grandparent, wrong')
for a, b in [('alice', 'bob'), ('alice', 'carol'), ('bob', 'dave'),
             ('carol', 'erin')]:
    +parent(a, b)

grandparent(X, Z) <= parent(X, Y) & parent(Y, Z)
wrong(X, Z) <= parent(X, Y) & parent(W, Z)   # W, not Y: nothing shared

print(len(grandparent(X, Z).data), 'pairs')
print(len(wrong(X, Z).data), 'pairs')
print(('alice', 'bob') in wrong(X, Z).data)
