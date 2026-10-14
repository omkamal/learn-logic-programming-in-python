from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, parent')
+parent('alice', 'bob')
+parent('alice', 'carol')

answer = parent('alice', X)
print(type(answer).__name__)
print(answer.data)          # list of tuples
print(answer.v())           # the FIRST ANSWER ROW, not a column
print(sorted(answer.v()))
print(bool(parent('alice', 'bob')), bool(parent('bob', 'alice')))
print(pyDatalog.ask("parent('alice', X)").answers)
pyDatalog.assert_fact('parent', 'bob', 'dave')
print(sorted(parent(X, Y).data))
pyDatalog.retract_fact('parent', 'bob', 'dave')
print(sorted(parent(X, Y).data))
