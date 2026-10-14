from pyDatalog import pyDatalog

pyDatalog.create_terms('X, N, price, big, too_soon')
+price('pen', 3)
+price('book', 12)

big(X) <= price(X, N) & (N > 5)          # fill N first, then check it
print(sorted(big(X).data))

too_soon(X) <= (N > 5) & price(X, N)     # check N while it is still blank
try:
    print(sorted(too_soon(X).data))
except Exception as err:
    print(type(err).__name__ + ':', str(err).splitlines()[0])
