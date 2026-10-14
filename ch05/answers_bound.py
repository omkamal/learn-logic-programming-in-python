from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, p, q, good, early')
for a, b in [(1, 2), (2, 3)]:
    +p(a, b)
for b, c in [(2, 4), (3, 5), (3, 1)]:
    +q(b, c)

good(X, Z) <= p(X, Y) & q(Y, Z) & (Z > 3)       # comparison last
print(sorted(good(X, Z).data))

early(X, Z) <= (Z > 3) & p(X, Y) & q(Y, Z)      # comparison first
try:
    print(sorted(early(X, Z).data))
except Exception as err:
    print(type(err).__name__ + ':', str(err).splitlines()[0])
