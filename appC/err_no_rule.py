import textwrap
from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Z, parent, grandparent')
+parent('alice', 'bob')

try:
    print(grandparent(X, Z))       # named, but no fact and no rule
except Exception as err:
    print(textwrap.fill(type(err).__name__ + ': ' + str(err), 74,
                        subsequent_indent='    '))
