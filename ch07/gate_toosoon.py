from pyDatalog import pyDatalog

pyDatalog.create_terms('X, N, S, price, big, too_soon, no_filler')
+price('pen', 3)
+price('book', 12)

big(X) <= price(X, N) & (N > 5)          # fill N first, then check it
print(sorted(big(X).data))

too_soon(X) <= (N > 5) & price(X, N)     # check N while it is still blank
try:
    print(sorted(too_soon(X).data))
except Exception as err:
    print(type(err).__name__ + ':', str(err).splitlines()[0])

no_filler(X) <= price(X, N) & (N > S)    # S is never filled by anything
try:
    print(sorted(no_filler(X).data))
except Exception as err:
    print(type(err).__name__ + ':', str(err).splitlines()[0])
