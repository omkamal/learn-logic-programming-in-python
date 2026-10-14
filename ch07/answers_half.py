from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, N, price, half, half_ok')
for item, cost in [('pen', 3), ('lamp', 5), ('mug', 7), ('book', 12)]:
    +price(item, cost)

half(X, Y) <= (Y == N // 2) & price(X, N)
print(sorted(half(X, Y).data))

half_ok(X, Y) <= price(X, N) & (Y == N // 2)
print(sorted(half_ok(X, Y).data))
