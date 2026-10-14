from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, N, A, B, price, big, five_up, cheaper,'
                       ' twice_big')

+price('pen', 3)
+price('book', 12)
+price('lamp', 5)
+price('mug', 7)

big(X) <= price(X, N) & (N > 5)
five_up(X) <= price(X, N) & (N >= 5)
cheaper(X, Y) <= price(X, A) & price(Y, B) & (A < B)
twice_big(X) <= price(X, N) & (N * 2 > 10)

print(sorted(big(X).data))
print(sorted(five_up(X).data))
print(len(cheaper(X, Y).data))
print(sorted(twice_big(X).data))
