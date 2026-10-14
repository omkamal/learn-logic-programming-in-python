# timeout: 8
from pyDatalog import pyDatalog

pyDatalog.create_terms('X, N, price, big')
+price('pen', 3)
+price('book', 12)

print('defining the rule ...')
big(X) <= price(X, N) & N > 5        # no brackets around N > 5
print('rule defined')
