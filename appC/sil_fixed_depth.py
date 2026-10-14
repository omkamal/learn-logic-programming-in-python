from pyDatalog import pyDatalog

pyDatalog.create_terms('W, X, Y, Z, parent, greatgp')
for a, b in [('alice', 'bob'), ('bob', 'carol'), ('carol', 'dave'),
             ('dave', 'eve')]:
    +parent(a, b)

greatgp(X, Z) <= parent(X, Y) & parent(Y, W) & parent(W, Z)
print(sorted(greatgp(X, Z).data))
print(bool(greatgp('alice', 'eve')))     # four steps: no rule reaches it
