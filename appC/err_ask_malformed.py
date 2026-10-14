from pyDatalog import pyDatalog

pyDatalog.create_terms('parent')
+parent('alice', 'bob')

try:
    pyDatalog.ask("parent('alice', X")      # the bracket is never closed
except Exception as err:
    print(type(err).__name__ + ':', err)
