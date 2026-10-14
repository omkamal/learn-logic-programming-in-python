from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, N, price, half, whole_half, rest, square')
+price('pen', 3)
+price('book', 12)

half(X, Y) <= price(X, N) & (Y == N / 2)
whole_half(X, Y) <= price(X, N) & (Y == N // 2)
rest(X, Y) <= price(X, N) & (Y == N % 5)
square(X, Y) <= price(X, N) & (Y == N ** 2)

print(sorted(half(X, Y).data))
print(sorted(whole_half(X, Y).data))
print(sorted(rest(X, Y).data))
print(sorted(square(X, Y).data))
