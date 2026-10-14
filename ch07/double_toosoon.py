from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, N, price, too_soon')
+price('pen', 3)
+price('book', 12)

too_soon(X, Y) <= (Y == N * 2) & price(X, N)    # compute while N is blank
print(sorted(too_soon(X, Y).data))
