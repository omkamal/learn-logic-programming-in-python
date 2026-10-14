from pyDatalog import pyDatalog

pyDatalog.create_terms('X, N, S, price, big')
+price('pen', 3)
+price('book', 12)

big(X) <= price(X, N) & (N > S)              # S is never filled
try:
    print(big(X))
except Exception as err:
    print(type(err).__name__ + ':', err)
