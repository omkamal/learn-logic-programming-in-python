from pyDatalog import pyDatalog

pyDatalog.create_terms('X, parent')
+parent('alice', 'bob')

try:
    print(parent(X))
except AttributeError as err:
    print('AttributeError:', err)
