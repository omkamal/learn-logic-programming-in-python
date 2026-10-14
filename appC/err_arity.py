import textwrap
from pyDatalog import pyDatalog

pyDatalog.create_terms('X, parent')
+parent('alice', 'bob')

try:
    print(parent(X))               # one slot, but parent has two
except Exception as err:
    print(textwrap.fill(type(err).__name__ + ': ' + str(err), 74,
                        subsequent_indent='    '))
