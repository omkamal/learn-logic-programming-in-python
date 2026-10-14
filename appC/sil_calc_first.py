from pyDatalog import pyDatalog

pyDatalog.create_terms('X, N, T, price, good, bad')
+price('pen', 3)
+price('book', 12)

good(X, T) <= price(X, N) & (T == N * 2)     # fill, then calculate
bad(X, T) <= (T == N * 2) & price(X, N)      # calculate, then fill

print(sorted(good(X, T).data))
print(sorted(bad(X, T).data))
