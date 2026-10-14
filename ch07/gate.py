from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, N, A, B, price, big, cheaper')

+price('pen', 3)
+price('book', 12)

big(X) <= price(X, N) & (N > 5)
cheaper(X, Y) <= price(X, A) & price(Y, B) & (A < B)

print(sorted(big(X).data))
print(sorted(cheaper(X, Y).data))
