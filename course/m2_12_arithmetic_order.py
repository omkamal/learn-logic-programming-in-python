from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, N, price, double, too_soon')
+price('pen', 3)
+price('book', 12)

double(X, Y) <= price(X, N) & (Y == N * 2)      # fill N first, then compute Y
print(sorted(double(X, Y).data))

too_soon(X, Y) <= (Y == N * 2) & price(X, N)    # compute while N is still blank
print(sorted(too_soon(X, Y).data))
