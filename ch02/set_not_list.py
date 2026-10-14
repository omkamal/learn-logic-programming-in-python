from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, parent')

+parent('alice', 'bob')
+parent('alice', 'bob')      # the very same card, a second time
+parent('alice', 'carol')

print(len(parent(X, Y).data), 'cards in the fact base')
