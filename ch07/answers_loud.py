from pyDatalog import pyDatalog

pyDatalog.create_terms('X, N, price, expensive, fixed')
for item, cost in [('pen', 3), ('lamp', 5), ('mug', 7), ('book', 12)]:
    +price(item, cost)

expensive(X) <= (N >= 10) & price(X, N)
try:
    print(sorted(expensive(X).data))
except Exception as err:
    print(type(err).__name__ + ':', str(err).splitlines()[0])

fixed(X) <= price(X, N) & (N >= 10)
print(sorted(fixed(X).data))
