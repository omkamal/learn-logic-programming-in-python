from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, parent')
+parent('alice', 'bob')
+parent('alice', 'carol')

pyDatalog.assert_fact('parent', 'bob', 'dave')
print(sorted(parent(X, Y).data))
pyDatalog.retract_fact('parent', 'bob', 'dave')
print(sorted(parent(X, Y).data))
pyDatalog.retract_fact('parent', 'zed', 'zoe')   # no such card
print(sorted(parent(X, Y).data))
-parent('alice', 'carol')                        # the minus form
print(sorted(parent(X, Y).data))
