from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, N, price, before')
+price('pen', 3)
+price('book', 12)

# "which Y is one less than the price?"  The unknown sits inside a sum.
before(X, Y) <= price(X, N) & (Y + 1 == N)
try:
    print(sorted(before(X, Y).data))
except Exception as err:
    print(type(err).__name__ + ':')
    print(' ', str(err).splitlines()[0])
