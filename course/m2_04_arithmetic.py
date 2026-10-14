from pyDatalog import pyDatalog

pyDatalog.create_terms('N, N1, F, F1, X, Y, factorial, fib, double, big, price')

# factorial: recursion + arithmetic
+(factorial[0] == 1)
factorial[N] = N * factorial[N - 1]
print(factorial[5] == F)
print(factorial[10] == F)

# fibonacci
+(fib[0] == 0)
+(fib[1] == 1)
fib[N] = fib[N - 1] + fib[N - 2]
print(fib[20] == F)

# arithmetic in a clause body
+price('pen', 3)
+price('book', 12)
double(X, Y) <= price(X, N) & (Y == N * 2)
print(sorted(double(X, Y).data))
big(X) <= price(X, N) & (N > 5)
print(big(X))
