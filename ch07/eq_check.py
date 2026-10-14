from pyDatalog import pyDatalog

pyDatalog.create_terms('X, N, price, exactly_12')
+price('pen', 3)
+price('book', 12)

# N already has a value from price(), so == only checks it
exactly_12(X) <= price(X, N) & (N == 12)
print(sorted(exactly_12(X).data))
