from pyDatalog import pyDatalog

pyDatalog.create_terms('W, X, Y, Z, parent, gp, gp_swapped')
pyDatalog.create_terms('g1, g2, g3, g4, g5, g6')

for a, b in [('alice', 'bob'), ('alice', 'carol'), ('bob', 'dave'),
             ('carol', 'erin'), ('dave', 'fay'), ('erin', 'gus'),
             ('erin', 'hal')]:
    +parent(a, b)

# two conditions, written in both orders
gp(X, Z) <= parent(X, Y) & parent(Y, Z)
gp_swapped(X, Z) <= parent(Y, Z) & parent(X, Y)
print(sorted(gp(X, Z).data) == sorted(gp_swapped(X, Z).data))

# three conditions: all six orders
g1(X, W) <= parent(X, Y) & parent(Y, Z) & parent(Z, W)
g2(X, W) <= parent(X, Y) & parent(Z, W) & parent(Y, Z)
g3(X, W) <= parent(Y, Z) & parent(X, Y) & parent(Z, W)
g4(X, W) <= parent(Y, Z) & parent(Z, W) & parent(X, Y)
g5(X, W) <= parent(Z, W) & parent(X, Y) & parent(Y, Z)
g6(X, W) <= parent(Z, W) & parent(Y, Z) & parent(X, Y)

results = [sorted(g(X, W).data) for g in (g1, g2, g3, g4, g5, g6)]
print('distinct answers among the six rules:',
      len({str(r) for r in results}))
print(results[0])
