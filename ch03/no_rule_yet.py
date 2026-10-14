from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, parent, grandparent')
+parent('alice', 'bob')
+parent('alice', 'carol')
+parent('bob', 'dave')
+parent('carol', 'erin')

try:
    print(grandparent(X, Y))
except AttributeError as err:
    print('AttributeError:')
    print(err)
