from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, parent')
+parent('alice', 'bob')
+parent('alice', 'carol')

answer = parent('alice', X)
print(type(answer).__name__)
print(answer.data)             # a plain list of tuples
print(sorted(answer.data))     # the same rows in a fixed order
print(parent('alice', 'bob').data)    # yes: one empty tuple
print(parent('bob', 'alice').data)    # no: no rows at all
print(bool(parent('alice', 'bob')), bool(parent('bob', 'alice')))
