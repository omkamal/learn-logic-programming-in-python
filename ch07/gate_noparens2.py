from pyDatalog import pyDatalog

pyDatalog.create_terms('X, N, price, big')
+price('pen', 3)
+price('book', 12)

try:
    big(X) <= N > 5 & price(X, N)    # no parentheses, comparison first
except Exception as err:
    print(type(err).__name__ + ':', str(err).splitlines()[0])
