from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, P, parent, with_neq, without_neq')

+parent('ola', 'ann')
+parent('ola', 'ben')
+parent('ola', 'cleo')
+parent('ann', 'dina')

with_neq(X, Y) <= parent(P, X) & parent(P, Y) & (X != Y)
without_neq(X, Y) <= parent(P, X) & parent(P, Y)

print(len(with_neq(X, Y).data), 'pairs with the inequality')
print(len(without_neq(X, Y).data), 'pairs without it')
