from pyDatalog import pyDatalog

pyDatalog.create_terms('X, N, price, gt, lt, ge, le, ne, eq')
+price('pen', 3)
+price('book', 12)

gt(X) <= price(X, N) & (N > 5)
lt(X) <= price(X, N) & (N < 5)
ge(X) <= price(X, N) & (N >= 12)
le(X) <= price(X, N) & (N <= 3)
ne(X) <= price(X, N) & (N != 3)
eq(X) <= price(X, N) & (N == 12)

for q in (gt(X), lt(X), ge(X), le(X), ne(X), eq(X)):
    print(sorted(q.data))
