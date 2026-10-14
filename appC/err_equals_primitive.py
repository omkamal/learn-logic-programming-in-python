import textwrap
from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, N, price, before')
+price('pen', 3)

before(X, Y) <= price(X, N) & (Y + 1 == N)       # equations are not solved
try:
    print(before(X, Y))
except Exception as err:
    print(textwrap.fill(type(err).__name__ + ': ' + str(err), 74,
                        subsequent_indent='    '))
