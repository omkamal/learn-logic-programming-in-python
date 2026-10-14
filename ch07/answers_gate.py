from pyDatalog import pyDatalog

pyDatalog.create_terms('X, N, price, affordable, at_most')
for item, cost in [('pen', 3), ('lamp', 5), ('mug', 7), ('book', 12)]:
    +price(item, cost)

affordable(X) <= price(X, N) & (N < 7)
at_most(X) <= price(X, N) & (N <= 7)
print(sorted(affordable(X).data))
print(sorted(at_most(X).data))
