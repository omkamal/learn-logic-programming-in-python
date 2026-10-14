from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, N, price, boxed')
+price('pen', 3)
+price('book', 12)

# a dozen of each, plus 5 for the box: each calculator uses the last one
boxed(X, Y, Z) <= price(X, N) & (Y == N * 12) & (Z == Y + 5)
print(sorted(boxed(X, Y, Z).data))
