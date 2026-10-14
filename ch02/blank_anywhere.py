from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, parent')

+parent('alice', 'bob')
+parent('alice', 'carol')
+parent('bob', 'dave')
+parent('carol', 'erin')

print(parent(X, 'dave'))    # blank in the first slot
print(parent(X, Y))         # two blanks: every card
print(parent('alice', 'bob'))   # no blanks: is there such a card?
print(parent('bob', 'alice'))
print(parent(X, X))         # one name used twice
