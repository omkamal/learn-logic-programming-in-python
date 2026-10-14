from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, loan')
+loan('mona', 'Maps of Salt')

try:
    print(loan(X))
except AttributeError as err:
    print('AttributeError:', err)

+loan('mona')                      # no error: a different table, loan/1
print(loan(X))
print(sorted(loan(X, Y).data))     # loan/2 is untouched
