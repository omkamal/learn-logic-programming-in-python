from pyDatalog import pyDatalog

pyDatalog.create_terms('P, X, Y, parent, sibling, sibling_bad')
for a, b in [('alice', 'bob'), ('alice', 'carol'), ('bob', 'dave'),
             ('carol', 'erin')]:
    +parent(a, b)

sibling(X, Y) <= parent(P, X) & parent(P, Y) & (X != Y)
sibling_bad(X, Y) <= parent(P, X) & parent(P, Y)     # no inequality

print(sorted(sibling(X, Y).data))
print(('bob', 'bob') in sibling_bad(X, Y).data, len(sibling_bad(X, Y).data),
      'pairs, 2 expected')
