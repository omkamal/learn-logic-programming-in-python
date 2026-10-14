from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, N, price, double')
+price('pen', 3)
+price('book', 12)

double(X, Y) <= price(X, N) & (Y == N * 2)      # fill N, then compute Y
print(sorted(double(X, Y).data))
